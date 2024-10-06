document.addEventListener('DOMContentLoaded', () => {
    const videoUrlInput = document.getElementById('video-url');
    const summarizeBtn = document.getElementById('summarize-btn');
    const summaryContent = document.getElementById('summary-content');
    const historyList = document.getElementById('history-list');
    const videoThumbnail = document.getElementById('video-thumbnail');
    const videoTitle = document.getElementById('video-title');

    let history = JSON.parse(localStorage.getItem('summaryHistory')) || [];

    function updateHistory() {
        historyList.innerHTML = '';
        history.forEach((item, index) => {
            const li = document.createElement('li');
            li.textContent = item.title || item.url;
            li.addEventListener('click', () => {
                videoUrlInput.value = item.url;
                displayVideoInfo(item);
                summaryContent.innerHTML = item.summary;
            });
            historyList.appendChild(li);
        });
    }

    function displayVideoInfo(videoData) {
        if (videoData.thumbnail) {
            videoThumbnail.src = videoData.thumbnail;
            videoThumbnail.style.display = 'block';
        } else {
            videoThumbnail.style.display = 'none';
        }
        videoTitle.textContent = videoData.title || '';
    }

    updateHistory();

    summarizeBtn.addEventListener('click', () => {
        const url = videoUrlInput.value.trim();
        if (!url) return;

        summarizeBtn.disabled = true;
        summaryContent.innerHTML = 'Generating summary...';

        fetch('/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                summaryContent.innerHTML = `Error: ${data.error}`;
            } else {
                summaryContent.innerHTML = data.summary.replace(/\n/g, '<br>');
                displayVideoInfo(data);
                history.unshift({
                    url,
                    summary: data.summary,
                    title: data.title,
                    thumbnail: data.thumbnail
                });
                if (history.length > 5) history.pop();
                localStorage.setItem('summaryHistory', JSON.stringify(history));
                updateHistory();
            }
        })
        .catch(error => {
            summaryContent.innerHTML = `Error: ${error.message}`;
        })
        .finally(() => {
            summarizeBtn.disabled = false;
        });
    });
});
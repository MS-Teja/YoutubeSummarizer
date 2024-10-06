from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# YouTube API key
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

app = Flask(__name__)

def extract_video_id(url):
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"(?:embed\/)([0-9A-Za-z_-]{11})",
        r"(?:shorts\/)([0-9A-Za-z_-]{11})",
        r"^([0-9A-Za-z_-]{11})$"
    ]

    parsed_url = urlparse(url)

    query = parse_qs(parsed_url.query)
    if 'v' in query:
        return query['v'][0]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None

def get_video_info(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if 'items' in data and len(data['items']) > 0:
        snippet = data['items'][0]['snippet']
        return {
            'title': snippet['title'],
            'thumbnail': snippet['thumbnails']['medium']['url']
        }
    return None

def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def summarize_text(text):
    try:
        prompt = f"""Analyze and summarize the following YouTube video transcript:

{text}

Provide a comprehensive summary of the video content using the following structure:

1. Main Topic: Briefly state the primary subject or theme of the video in one sentence.

2. Key Points: List the 3-5 most important ideas or arguments presented in the video.

3. Detailed Summary: In 2-3 paragraphs, provide a more in-depth summary of the video's content, including any significant examples, case studies, or data mentioned.

4. Notable Quotes: Extract 2-3 significant or memorable quotes from the transcript, if any.

5. Conclusion: Summarize the main takeaway or conclusion of the video in 1-2 sentences.

6. Target Audience: Briefly mention who would find this video most useful or interesting.

Please ensure the summary is concise yet informative, capturing the essence of the video content."""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert at analyzing and summarizing video content."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.json['url']
    video_id = extract_video_id(url)

    if not video_id:
        return jsonify({'error': 'Invalid YouTube URL'}), 400

    video_info = get_video_info(video_id)
    if not video_info:
        return jsonify({'error': 'Failed to fetch video information'}), 400

    transcript = get_video_transcript(video_id)

    if not transcript:
        return jsonify({'error': 'Failed to fetch video transcript'}), 400

    summary = summarize_text(transcript)

    if not summary:
        return jsonify({'error': 'Failed to generate summary'}), 500

    return jsonify({
        'summary': summary,
        'title': video_info['title'],
        'thumbnail': video_info['thumbnail']
    })

if __name__ == '__main__':
    app.run(debug=True)
# YouTube Video Summarizer

YouTube Video Summarizer is a web application that automatically generates concise summaries of YouTube videos using their transcripts. It leverages the power of AI to provide users with quick insights into video content without watching the entire video.

## Features

- Summarize YouTube videos by simply entering the video URL
- Display video thumbnail and title for easy identification
- Provide a structured summary including:
  - Main topic
  - Key points
  - Detailed summary
  - Notable quotes
  - Conclusion
  - Target audience
- Maintain a history of summarized videos for quick access
- Modern, responsive user interface

## Technologies Used

- Backend: Python with Flask
- Frontend: HTML, CSS, JavaScript
- AI: OpenAI GPT model for summarization
- APIs: YouTube Data API, YouTube Transcript API

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/MS-Teja/YoutubeVideoSummarizer.git
   cd YoutubeVideoSummarizer
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Enter a YouTube video URL in the input field.
2. Click the "Summarize" button.
3. Wait for the summary to be generated.
4. View the video information, including thumbnail and title.
5. Read the structured summary of the video content.
6. Access previously summarized videos from the history section.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing the GPT model
- YouTube Data API and YouTube Transcript API for video data and transcripts
- Flask framework for the web application

## Contact

If you have any questions, feel free to reach out to [Teja](mailto:sivatejamutyala@gmail.com).
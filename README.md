# YouTube Video Summarizer

YouTube Video Summarizer is a web application that automatically generates concise summaries of YouTube videos using their transcripts. It leverages the power of AI to provide users with quick insights into video content without watching the entire video.

## Features

- Summarize YouTube videos by simply entering the video URL
- Display video thumbnail and title for easy identification
- Provide a structured summary including main topic, key points, detailed summary, notable quotes, conclusion, and target audience
- Maintain a history of summarized videos for quick access
- Modern, responsive user interface
- Secure access with username and password authentication

## Technologies Used

- Backend: Python with Flask
- Frontend: HTML, CSS, JavaScript
- AI: OpenAI GPT model for summarization
- APIs: YouTube Data API, YouTube Transcript API
- Containerization: Docker
- Deployment: Render

## Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/youtube-video-summarizer.git
   cd youtube-video-summarizer
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
   AUTH_USERNAME=your_chosen_username
   AUTH_PASSWORD=your_chosen_password
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open a web browser and navigate to `http://localhost:5000`

## Docker Setup

1. Build the Docker image:
   ```
   docker build -t youtube-summarizer .
   ```

2. Run the Docker container:
   ```
   docker run -p 5000:5000 --env-file .env youtube-summarizer
   ```

3. Access the application at `http://localhost:5000`

## Usage

1. Access the application using your username and password.
2. Enter a YouTube video URL in the input field.
3. Click the "Summarize" button.
4. Wait for the summary to be generated.
5. View the video information, including thumbnail and title.
6. Read the structured summary of the video content.
7. Access previously summarized videos from the history section.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing the GPT model
- YouTube Data API and YouTube Transcript API for video data and transcripts
- Flask framework for the web application

## Contact

If you have any questions, feel free to reach out to [Your Name](mailto:your.email@example.com).
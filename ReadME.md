# LinkedIn Resume HTML Generator

## Approach and Solution

### Problem Overview

The primary goal of this project is to create a web application that can convert a LinkedIn resume PDF into a structured HTML document. The challenge involves extracting text from a PDF and transforming it into a well-formatted HTML resume using the OpenAI API.

### Approach

1. **Setting Up the Environment:**

   - We used Flask to build a web application that handles file uploads and interacts with the OpenAI API.
   - PyPDF2 is utilized to extract text from PDF files, which is a crucial step in transforming the PDF resume into HTML.

2. **Handling File Uploads:**

   - The Flask application accepts PDF files via an upload form. Once a file is uploaded, it is processed to extract text content.

3. **Extracting Text from PDF:**

   - The `extract_text_from_pdf` function reads the uploaded PDF file and concatenates text from each page. This step ensures that all relevant text content is captured.

4. **Generating HTML with OpenAI API:**

   - With the extracted text, we use OpenAI’s GPT-4 API to generate HTML content. The API is prompted to convert the plain text resume into a structured HTML format.
   - The `generate_html_resume` function sends a request to the OpenAI API, and the response contains the HTML content that is then saved as an HTML file.

5. **Handling API Keys:**

   - Users are required to provide their OpenAI API key through a dedicated endpoint (`/set_api_key`). This key is used to authenticate requests to the OpenAI API.

### Solution

The solution involves integrating several components:

- **Flask Web Framework:** To manage file uploads and handle web requests.
- **PyPDF2:** For extracting text from PDF files.
- **OpenAI GPT-4 API:** To convert plain text into HTML format.
- **File Handling:** Saving the generated HTML file and providing it for download.

By combining these technologies, the web application effectively transforms a LinkedIn PDF resume into a structured HTML document that can be easily downloaded and used.

## Overview

This project provides a simple web application that converts a LinkedIn resume PDF into a structured HTML resume using OpenAI's GPT-4 API. The web app allows users to upload a LinkedIn PDF resume, which is then processed and converted into an HTML file.

## Features

- Upload a LinkedIn PDF resume.
- Convert the resume to a structured HTML format.
- Download the generated HTML resume.

## Requirements

- Python 3.7+
- Flask
- PyPDF2
- OpenAI Python client

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/varshithbollam/linkedin-resume-html-generator.git
   cd linkedin-resume-html-generator
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**

   - Ensure that your OpenAI API key is set. You can do this dynamically through the web app.

4. **Run the Application:**

   ```bash
   python app.py
   ```

   The application will start at `http://127.0.0.1:5000/`.

## Usage

1. **Open the Web Application:**

   Visit `http://127.0.0.1:5000/` in your web browser.

2. **Set API Key:**

   - Navigate to the `/set_api_key` endpoint to input your OpenAI API key. This will initialize the API client for further operations.

3. **Upload Resume:**

   - Go to the `/` route and use the form to upload your LinkedIn resume in PDF format.

4. **Download HTML Resume:**

   - After the PDF is processed, you will be able to download the generated HTML resume.

## Troubleshooting

- **No file part / No selected file**: Ensure you are selecting a valid PDF file.
- **OpenAI API key not set!**: Make sure you have set the OpenAI API key by visiting `/set_api_key`.
- **Error generating HTML**: Check if your OpenAI API key is valid and try again.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any issues or feature requests, please contact [your email address] or open an issue on the GitHub repository.

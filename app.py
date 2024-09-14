import os
from flask import Flask, render_template, request, send_file
import PyPDF2
from openai import OpenAI

app = Flask(__name__)

# Set OpenAI API key dynamically at app start
openai_api_key = None
client = None  # Initialize client here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_api_key', methods=['POST'])
def set_api_key():
    global openai_api_key
    global client
    openai_api_key = request.form['api_key']
    os.environ["OPENAI_API_KEY"] = openai_api_key
    client = OpenAI()  # Initialize OpenAI client with the provided API key
    return "API Key Set", 200

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.endswith('.pdf'):
        # Extract text from PDF
        pdf_text = extract_text_from_pdf(file)
        
        # Process with OpenAI API
        html_resume = generate_html_resume(pdf_text)
        
        # Save the HTML file and return
        output_path = "resume.html"
        with open(output_path, "w") as f:
            f.write(html_resume)
        
        return send_file(output_path, as_attachment=True)

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def generate_html_resume(pdf_text):
    if not openai_api_key:
        return "OpenAI API key not set!", 500

    # Use the updated OpenAI client to create the chat completion
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Convert the following resume text to a structured HTML resume:\n\n{pdf_text}"}]
        )
        html_resume = chat_completion['choices'][0]['message']['content'].strip()
        return html_resume
    except Exception as e:
        return f"Error generating HTML: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

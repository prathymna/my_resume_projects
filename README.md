# 🚀 AI-Powered Applicant Tracking System (ATS) & Resume Screening Platform

An enterprise-grade, full-stack web application designed to automate and streamline the corporate recruitment process. This platform leverages Artificial Intelligence (OpenAI LLMs) and Natural Language Processing (NLP) to parse candidate PDF resumes, perform semantic matching against dynamic job descriptions, and generate structured HR evaluation reports.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Flask-SQLAlchemy
* **AI Engine:** OpenAI API (`gpt-4o-mini`), PyPDF2 (PDF Text Extraction)
* **Database:** SQLite (Relational Data Persistence)
* **API Architecture:** RESTful JSON endpoints (`/api/candidates`)
* **Frontend:** HTML5, CSS3 (Modern Responsive UI)

---

## ✨ Key Features

1. **Dynamic Job Description Matching:** Recruiters can input custom job descriptions and role requirements on the fly for targeted candidate evaluations.
2. **AI Semantic Evaluation:** Contextually analyzes resumes against job requirements (providing overall match scores, matching skills, skill gaps, and final hire/reject verdicts) instead of relying on brittle keyword matching.
3. **Automated PDF Parsing:** Extracts and processes raw text directly from uploaded PDF candidate resumes.
4. **Candidate Database & Dashboard:** Securely stores candidate records, uploaded filenames, target job descriptions, and AI evaluation reports using SQLite and SQLAlchemy.
5. **REST API Endpoint:** Exposes a JSON-compliant API route (`/api/candidates`) for integration with external services or automated pipelines.
6. **Full CRUD Support:** Features a responsive HR dashboard with candidate record management and deletion capabilities.

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git)

cd YOUR-REPOSITORY-NAME
2. Install Dependencies
Bash
pip install flask flask-sqlalchemy openai python-dotenv PyPDF2

3. Set Up Environment Variables
Create a .env file in the root directory of your project and add your OpenAI API key:

Code snippet
OPENAI_API_KEY=your_actual_openai_api_key_here
(Make sure .env is included in your .gitignore file to protect your credentials).

4. Run the Application
Bash
python app.py
Open your web browser and navigate to: http://127.0.0.1:5001

📌 API Endpoints Reference
GET / - Main Web UI for uploading resumes and defining custom job descriptions.

GET /dashboard - HR dashboard view listing all stored candidate evaluations with management tools.

POST /delete/<id> - Securely deletes a specific candidate record from the database.

GET /api/candidates - REST API endpoint returning all stored candidate assessments in structured JSON format.
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import PyPDF2
import main

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ats_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Table
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.Text, nullable=True)
    scan_result = db.Column(db.Text, nullable=False)

# Create tables
with app.app_context():
    db.create_all()


# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        uploaded_file = request.files.get('resume_file')
        custom_job_description = request.form.get('job_description', 'General Software Developer')
        
        if uploaded_file and uploaded_file.filename != '':
            # 1. Read PDF
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            extracted_text = ""
            for page in pdf_reader.pages:
                extracted_text += page.extract_text()
                
            # 2. Run AI Engine with dynamic job description
            final_scan_output = main.evaluate_resume(extracted_text, custom_job_description)
            
            # 3. Save to Database
            new_record = Candidate(
                filename=uploaded_file.filename, 
                job_description=custom_job_description,
                scan_result=final_scan_output
            )
            db.session.add(new_record)
            db.session.commit()
            
            result = final_scan_output

    return render_template('index.html', result=result)


@app.route('/dashboard')
def dashboard():
    all_candidates = Candidate.query.all()
    return render_template('dashboard.html', candidates=all_candidates)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_candidate(id):
    candidate_to_delete = Candidate.query.get_or_404(id)
    try:
        db.session.delete(candidate_to_delete)
        db.session.commit()
        return redirect(url_for('dashboard'))
    except:
        return "There was a problem deleting that candidate."


# --- REST API ENDPOINT ---
@app.route('/api/candidates', methods=['GET'])
def get_candidates_api():
    candidates = Candidate.query.all()
    candidate_list = [
        {
            "id": c.id, 
            "filename": c.filename, 
            "job_description": c.job_description,
            "scan_result": c.scan_result
        } 
        for c in candidates
    ]
    return jsonify({"success": True, "count": len(candidate_list), "data": candidate_list})


if __name__ == '__main__':
    print(">>> STARTING AI ATS SERVER ON PORT 5001 <<<")
    app.run(debug=True, port=5001)
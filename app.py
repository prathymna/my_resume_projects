from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import PyPDF2
import main
import data

app = Flask(__name__)

# --- DATABASE CONFIGURATION ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ats_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Table
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    scan_result = db.Column(db.Text, nullable=False)

# Create tables
with app.app_context():
    db.create_all()


# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        uploaded_file = request.files['resume_file']
        
        if uploaded_file.filename != '':
            # 1. Read PDF
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            extracted_text = ""
            for page in pdf_reader.pages:
                extracted_text += page.extract_text()
                
            # 2. Run Engine
            final_scan_output = main.evaluate_resume(extracted_text, data.required_skills)
            
            # 3. Save to Database
            new_record = Candidate(filename=uploaded_file.filename, scan_result=final_scan_output)
            db.session.add(new_record)
            db.session.commit()
            
            return render_template('index.html', result=final_scan_output)

    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    # Fetch all candidates and send to dashboard.html
    all_candidates = Candidate.query.all()
    return render_template('dashboard.html', candidates=all_candidates)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_candidate(id):
    # Find the candidate by their ID, or return a 404 error if they don't exist
    candidate_to_delete = Candidate.query.get_or_404(id)
    
    try:
        # Delete from database and save changes
        db.session.delete(candidate_to_delete)
        db.session.commit()
        # Refresh the dashboard
        return redirect(url_for('dashboard'))
    except:
        return "There was a problem deleting that candidate."


if __name__ == '__main__':
    # Changed port to 5001 to force a completely new server instance
    print(">>> STARTING ATS SERVER ON PORT 5001 <<<")
    print(">>> DASHBOARD ROUTE IS ACTIVE <<<")
    app.run(debug=True, port=5001)
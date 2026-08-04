import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client automatically using the key from .env
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def evaluate_resume(resume_text, required_skills):
    # Format the skills list nicely into a string
    skills_str = ", ".join(required_skills)
    
    # Craft the prompt for the AI
    prompt = f"""
    You are an expert AI Applicant Tracking System (ATS) and Senior Technical Recruiter. 
    Analyze the candidate resume provided below against the required skills/job description.
    
    Required Skills / Job Focus:
    {skills_str}
    
    Candidate Resume Text:
    {resume_text}
    
    Please provide a professional, structured evaluation report containing:
    1. Overall Match Score (Out of 100)
    2. Matching Skills Found in the Resume
    3. Missing Skills / Gaps
    4. Final Recruitment Verdict (Shortlist or Reject, with a brief justification)
    
    Keep the layout clean, professional, and easy for an HR manager to read.
    """

    try:
        # Call the OpenAI API using gpt-4o-mini
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional corporate recruiter and ATS engine."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        
        # Return the AI's response text
        return response.choices[0].message.content

    except Exception as e:
        return f"Error communicating with OpenAI API: {str(e)}"
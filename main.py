def evaluate_resume(resume_text, skills):
    # 1. Create an empty list to hold each line of our report
    report_lines = []
    
    report_lines.append("Scanning Resume...\n")
    
    found_count = 0
    total_skills = len(skills)
    
    # Convert resume text to lowercase once for accurate matching
    resume_text_lower = resume_text.lower()
    
    # 2. Loop through skills and append the results to our report list
    for skill in skills:
        if skill.lower() in resume_text_lower:
            report_lines.append(f"✅ Found: {skill}")
            found_count += 1
        else:
            report_lines.append(f"❌ Missing: {skill}")
            
    # 3. Calculate the match score
    if total_skills > 0:
        score = int((found_count / total_skills) * 100)
    else:
        score = 0
        
    # 4. Append the final score and status to the report
    report_lines.append("\n--- Final ATS Report ---")
    report_lines.append(f"Match Score: {score}%")
    
    if score >= 50:
        report_lines.append("Status: 🟢 INTERVIEW SELECTED")
    else:
        report_lines.append("Status: 🔴 REJECTED")
        
    # 5. THE CRITICAL FIX: Join all the lines together with a line break (\n) 
    # and RETURN the final text so app.py can send it to the HTML webpage.
    return "\n".join(report_lines)
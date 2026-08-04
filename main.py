# main.py
import data

# 1. We DEFINE the function (building the blender)
def evaluate_resume(resume_text, required_skills):
    print("Scanning Resume...\n")
    match_count = 0
    total_skills = len(required_skills)
    resume_lower = resume_text.lower()

    # Notice how this code is indented? That means it belongs inside the function.
    for skill in required_skills:
        if skill in resume_lower:
            print(f"✅ Found: {skill.capitalize()}")
            match_count += 1
        else:
            print(f"❌ Missing: {skill.capitalize()}")

    raw_percentage = (match_count / total_skills) * 100
    final_score = round(raw_percentage)

    print("\n--- Final ATS Report ---")
    print(f"Match Score: {final_score}%")

    if final_score >= 50:
        print("Status: 🟢 INTERVIEW SELECTED\n")
    else:
        print("Status: 🔴 REJECTED\n")

# 2. We CALL the function (pressing the run button)
# We pour our data from data.py into the engine
evaluate_resume(data.resume_text, data.required_skills)
print("\n--- Scanning Candidate 2 ---")
evaluate_resume(data.resume_text_2, data.required_skills)
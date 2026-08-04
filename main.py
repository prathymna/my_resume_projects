# main.py
import data  # This connects to your data.py file!

print("Scanning Resume...\n")

match_count = 0
# Notice how we type 'data.' before the variable names now
total_skills = len(data.required_skills)
resume_lower = data.resume_text.lower()

for skill in data.required_skills:
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
    print("Status: 🟢 INTERVIEW SELECTED")
else:
    print("Status: 🔴 REJECTED")
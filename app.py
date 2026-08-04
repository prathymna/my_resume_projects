from flask import Flask, render_template, request
# Import your actual ATS engine from your main.py file!
from main import evaluate_resume 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    scan_result = None  # By default, there is no result to show
    
    if request.method == 'POST':
        submitted_resume = request.form['resume_input']
        
        # Instead of just printing, we feed the text into your engine!
        scan_result = evaluate_resume(submitted_resume)
        
    # We pass the result back to the HTML page
    return render_template('index.html', result=scan_result)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

# Simple recommendation logic
recommendations = {
    "music": ["songwriting", "dj-ing"],
    "reading": ["writing", "poetry"],
    "gaming": ["game development", "streaming"],
    "traveling": ["photography", "blogging"],
    "cooking": ["baking", "food styling"],
    "sports": ["fitness training", "cycling"],
    "painting": ["digital art", "graphic design"]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    hobby1 = request.form.get('hobby1', '').strip().lower()
    hobby2 = request.form.get('hobby2', '').strip().lower()
    hobby3 = request.form.get('hobby3', '').strip().lower()

    all_recs = []
    for h in [hobby1, hobby2, hobby3]:
        if h in recommendations:
            all_recs.extend(recommendations[h])

    # Remove duplicates while preserving order
    final_recs = list(dict.fromkeys(all_recs))[:2]
    if not final_recs:
        final_recs = ["Try volunteering", "Learn photography"]

    return render_template('result.html', recs=final_recs)

if __name__ == '__main__':
    # Use port 10000 for Render compatibility; host 0.0.0.0 to accept external traffic
    app.run(host='0.0.0.0', port=10000, debug=True)

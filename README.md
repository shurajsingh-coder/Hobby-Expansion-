# Hobby Expansion

A small Flask web app that recommends 2 new hobbies based on the user's top 3 hobbies.

## How to run locally

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

Open http://127.0.0.1:10000 in your browser.

## Deploying to Render

1. Push this project to GitHub.
2. On Render, create a new **Web Service** and connect the GitHub repo.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app`
5. Deploy and you will get a public link.

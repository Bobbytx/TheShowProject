Create and activate virtual environment:

python3 -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

Install dependencies:

pip install -r requirements.txt

Run the app:

flask --app server.py run

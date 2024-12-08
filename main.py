
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Vercel expects this handler
def handler(request):
    return app(request)

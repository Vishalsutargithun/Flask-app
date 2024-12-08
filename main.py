from flask import Flask
from vercel import Function

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Comment this out since Vercel handles this serverless
    # app.run(host='0.0.0.0', port=5000, debug=True)
    pass

# Vercel expects a serverless function to be exported
handler = Function(app)

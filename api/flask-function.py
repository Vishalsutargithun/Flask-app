from flask import Flask, request

from vercel import Vercel

app = Flask(__name__)

@app.route('/')

def hello():

return 'Hello, World!'

if __name__ == '__main__':

app.run()

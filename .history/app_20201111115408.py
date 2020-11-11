from flask import Flask

app= Flask(__name__)

@app.route('/')
def home():
  return "<h1>Hello World</h1>"

app.run(port=3000)
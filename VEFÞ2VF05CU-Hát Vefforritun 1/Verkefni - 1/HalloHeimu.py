from flask import Flask

app = Flask(__name__)

@app.route("/")
def hallo():
    return "<h1>Hello world<h1> <img src='https://picsum.photos/200'>"

if __name__ == "__main__":
    app.run()
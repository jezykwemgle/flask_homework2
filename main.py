from flask import Flask

app = Flask(__name__)


@app.route('/')
def requirements():
    with open('requirements.txt', 'r') as file:
        out = file.read().replace('\n', '<br>')
    return f"Requirements:<br> {out}"


if __name__ == '__main__':
    app.run()

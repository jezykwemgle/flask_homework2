from flask import Flask
from faker import Faker

app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as file:
        out = file.read().replace('\n', '<br>')
    return f"Requirements:<br> {out}"


@app.route('/generate-users/')
def generate_users():

    return ''


@app.route('/mean/')
def mean():
    return ''


@app.route('/space/')
def space():
    return ''


if __name__ == '__main__':
    app.run()

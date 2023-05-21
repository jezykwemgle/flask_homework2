from flask import Flask
from flask import request
from faker import Faker
import itertools

app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as file:
        out = file.read().replace('\n', '<br>')
    return f"Requirements:<br> {out}"


@app.route('/generate-users/', methods=['GET', 'POST'])
def generate_users():
    fake = Faker()
    names, emails = [], []
    result = ''
    for _ in range(request.args.get('count', default=1, type=int)):
        names.append(f'{fake.name()}')
    names_emails = [f"{item[0]}: {item[1]}" for item in itertools.zip_longest(names, [f"{item.lower().replace(' ', '')}@gmail.com" for item in names])]
    for person in names_emails: result += f'{person}<br>'
    return result


@app.route('/mean/')
def mean():
    return ''


@app.route('/space/')
def space():
    return ''


if __name__ == '__main__':
    app.run()

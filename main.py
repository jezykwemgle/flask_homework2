from flask import Flask
from flask import request
from faker import Faker
import requests
import csv
import itertools

app = Flask(__name__)

@app.route('/')
def main():
    return 'START HERE'

@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as file:
        output = file.read().replace('\n', '<br>')
    return f"Requirements:<br> {output}"


@app.route('/generate-users/', methods=['GET', 'POST'])
def generate_users():
    fake = Faker()
    names = []
    result = ''
    for _ in range(request.args.get('count', default=1, type=int)):
        names.append(f'{fake.name()}')
    names_emails = [f"{item[0]}: {item[1]}" for item in itertools.zip_longest(names, [f"{item.lower().replace(' ', '')}@gmail.com" for item in names])]
    for person in names_emails: result += f'{person}<br>'
    return result


@app.route('/mean/')
def mean():
    with open('hw.csv', newline='') as csv_file:
        data = list(csv.reader(csv_file))
        sum_high = 0
        sum_weight = 0
        for i in range(1, len(data)-1):
            sum_high += float(data[i][1])*2.54
            sum_weight += float(data[i][2])/2.2046
    return f'Аverage heigh: {round(sum_high/len(data))}<br>Average weight: {round(sum_weight/len(data))}'


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json').json()
    return f"The number of astronauts at the moment: {str(r['number'])}"


if __name__ == '__main__':
    app.run()

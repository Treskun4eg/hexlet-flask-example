from random import randint
import json


def validate(user):
    errors = {}
    if not user.get('Nickname'):
        errors['Nickname'] = "Can't be blank"
    if not user.get('Email'):
        errors['Email'] = "Can't be blank"
    return errors


def save_form(repo, user):
    user['id'] = randint(1, 100)
    data = json.load(open(repo))
    data.append(user)
    with open(repo, 'w') as file:
        f = json.dumps(data)
        file.write(f)

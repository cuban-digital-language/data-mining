import os
import json


def get_text(path=''):
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), f'{path}facebook')):
        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'{path}facebook/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                try:
                    text.append(obj['text'])
                except:
                    pass

    return text


def get_details_text(path=""):
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), f'{path}facebook')):
        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'{path}facebook/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                try:
                    text.append((obj['text'], obj['date'], None))
                except:
                    pass

    return text

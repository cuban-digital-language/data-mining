import json


def get_text():
    f = open('data/cubadebate.json')
    data = json.load(f)

    text = []
    for obj in data:
        text.append(obj['text'])
        for c in obj['comments']:
            text.append(c['text'])

    return text


def get_details_text():
    f = open('data/cubadebate.json')
    data = json.load(f)

    text = []
    for obj in data:
        text.append((obj['text'], obj['date'], None))
        for c in obj['comments']:
            text.append((c['text'], c['date'], None))

    return text

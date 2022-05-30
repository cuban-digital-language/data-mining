import json


def get_text():
    f = open('data/twitter.json')
    data = json.load(f)

    user = set()
    text = []
    for obj in data:
        text.append(obj['text'])
        if obj['author'] in user:
            continue
        text.append(obj['raw_description'])
        if obj['raw_description'] != obj['description']:
            text.append(obj['description'])

    return text


def get_details_text():
    f = open('data/twitter.json')
    data = json.load(f)

    user = set()
    text = []
    for obj in data:
        text.append((obj['text'], obj['date'], None))

    return text

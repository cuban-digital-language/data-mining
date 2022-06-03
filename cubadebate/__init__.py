import json


def get_text(path=''):
    f = open(f'{path}cubadebate/cubadebate.json')
    data = json.load(f)

    text = []
    for obj in data:
        text.append((obj['text'], 'CubaDebate'))
        for c in obj['comments']:
            text.append((c['text'], 'CubaDebate'))

    return text


def get_details_text(path=''):
    f = open(f'{path}cubadebate/cubadebate.json')
    data = json.load(f)

    text = []
    for obj in data:
        text.append((obj['text'], obj['date'], 'CubaDebate'))
        for c in obj['comments']:
            text.append((c['text'], c['date'], 'CubaDebate'))

    return text

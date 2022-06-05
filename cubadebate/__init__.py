import json
import os


# def get_text(path=''):
#     f = open(f'{path}cubadebate/cubadebate.json')
#     data = json.load(f)

#     text = []
#     for obj in data:
#         text.append((obj['text'], 'CubaDebate'))
#         for c in obj['comments']:
#             text.append((c['text'], 'CubaDebate'))

#     return text


# def get_details_text(path=''):
#     f = open(f'{path}cubadebate/cubadebate.json')
#     data = json.load(f)

#     text = []
#     for obj in data:
#         text.append((obj['text'], obj['date'], 'CubaDebate'))
#         for c in obj['comments']:
#             text.append((c['text'], c['date'], 'CubaDebate'))

#     return text


def get_text(path=''):
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), f'{path}cubadebate')):
        if not filename.endswith('.json'):
            continue
        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'{path}cubadebate/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                try:
                    text.append((obj['text'], 'CubaDebate'))
                    for c in obj['comments']:
                        text.append((c['text'], 'CubaDebate'))
                except:
                    pass

    return text


def get_details_text(path=''):
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), f'{path}cubadebate')):
        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'{path}cubadebate/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                try:
                    text.append((obj['text'], obj['date'], 'CubaDebate'))
                    for c in obj['comments']:
                        text.append((c['text'], c['date'], 'CubaDebate'))
                except:
                    pass

    return text

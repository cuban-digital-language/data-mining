import os
import json


def get_text(path=''):
    text = []
    s = set()
    for filename in os.listdir(os.path.join(os.getcwd(), f'{path}facebook')):

        if not filename.endswith('.json'):
            continue

        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'{path}facebook/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                if obj['url'] in s:
                    continue
                s.add(obj['url'])
                try:
                    text.append((obj['text'], 'Facebook'))
                    for comment in obj['comment']:
                        text.append(
                            (comment['text'], 'Facebook'))
                except:
                    pass

    return text


def get_details_text(path=""):
    text = []
    s = set()

    for filename in os.listdir(os.path.join(os.getcwd(), f'{path}facebook')):
        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'{path}facebook/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                if obj['url'] in s:
                    continue
                s.add(obj['url'])
                try:
                    text.append((obj['text'], obj['date'], 'Facebook'))
                    for comment in obj['comment']:
                        text.append(
                            (comment['text'], comment['date'], 'Facebook'))
                except:
                    pass

    return text

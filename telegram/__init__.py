import os
import json


def get_text():
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), 'data/telegram')):
        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                try:
                    text.append(obj['message'])
                except:
                    pass

    return text


def get_details_text():
    text = []

    for filename in os.listdir(os.path.join(os.getcwd(), 'data/telegram')):
        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for obj in data:
                try:
                    text.append((obj['message'], obj['date'], None))
                except:
                    pass

    return text


def splitFile():
    file1 = []
    file2 = []
    for filename in os.listdir(os.path.join(os.getcwd(), 'data/telegram')):
        # open in readonly mode
        with open(os.path.join(os.getcwd(), f'data/telegram/{filename}'), 'r') as f:
            try:
                data = json.load(f)
            except:
                continue

            for i, obj in enumerate(data):
                try:
                    if i < len(data) / 2:
                        file1.append(obj)
                    else:
                        file2.append(obj)

                except:
                    pass

        with open(os.path.join(os.getcwd(), f'data/telegram/newData/{filename}1.json'), 'w') as f:
            f.write(json.dumps(file1))

        with open(os.path.join(os.getcwd(), f'data/telegram/newData/{filename}2.json'), 'w') as f:
            f.write(json.dumps(file1))


text = get_details_text()
# splitFile()

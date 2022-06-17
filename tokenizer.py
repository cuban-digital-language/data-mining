
try:
    from . import facebook as fb
    from . import cubadebate as cu
    from . import telegram as tg
    from . import twitter as tw
    from .tokenizer.custom_tokenizer import SpacyCustomTokenizer, get_progressbar
except (ModuleNotFoundError, ImportError):
    import facebook as fb
    import cubadebate as cu
    import telegram as tg
    import twitter as tw
    from tokenizer.custom_tokenizer import SpacyCustomTokenizer, get_progressbar


def get_all_text(path=''):
    return fb.get_text(path) + tg.get_text(path) + tw.get_text(path) + cu.get_text(path)


print("------  Init Tokenizer  ----------")
texts = get_all_text('')
print("------  Load Tokenizer  ----------")
nlp = SpacyCustomTokenizer()
nlp.__load__()

print("------  Init Process  ----------")
bar = get_progressbar(len(texts))
bar.start()
i = 0
for text, _ in texts:
    i += 1
    for token in nlp(text):
        pass
    bar.update(i)
bar.finish()

nlp.__save__()

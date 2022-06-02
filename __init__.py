try:
    from . import facebook as fb
    from . import cubadebate as cu
    from . import telegram as tg
    from . import twitter as tw
except (ModuleNotFoundError, ImportError):
    import facebook as fb
    import cubadebate as cu
    import telegram as tg
    import twitter as tw


def get_all_text(path=''):
    return fb.get_text(path) + tg.get_text(path) + tw.get_text(path) + cu.get_text(path)

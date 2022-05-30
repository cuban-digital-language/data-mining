try:
    import .facebook as fb
    import .cubadebate as cu
    import .telegram as tg
    import .twitter as tw
except ModuleNotFoundError:
    import facebook as fb
    import cubadebate as cu
    import telegram as tg
    import twitter as tw


def get_all_text():
    return fb.get_text() + tg.get_text() + tw.get_text() + cu.get_text()

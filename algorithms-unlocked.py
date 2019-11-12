from search.searcher import Linear
from search.searcher import BetterLinear


def _run():
    l = Linear()
    l.load_data()
    l.search("Old Man and the Sea")

    bl = BetterLinear()
    bl.load_data()
    bl.search("Old Man and the Sea")


if __name__ == '__main__':
    _run()

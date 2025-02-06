def game():
    from .logic.data import load_data
    load_data()
    from . import main
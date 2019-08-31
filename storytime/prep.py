from pippi import dsp
from storytime.recipes import RECIPES

def one(db, src):
    return dsp.choice(RECIPES)(db, src)

def many(count, db, src):
    for _ in range(count):
        yield one(db, src)


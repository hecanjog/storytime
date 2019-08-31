from pippi import dsp
from storytime.crops import CROPS

def grow(db, length=10):
    return dsp.choice(CROPS)(db, length)

def harvest(count, db, length=10):
    for _ in range(count):
        yield grow(db, length)


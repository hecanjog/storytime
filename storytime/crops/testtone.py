from pippi import dsp, oscs

def execute(db, length=10):
    return oscs.Osc('rnd', freq=dsp.rand(50, 500)).play(length) * 0.2

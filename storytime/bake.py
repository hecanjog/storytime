from pippi import dsp, fx

def mix(ingredients, length):
    out = dsp.buffer(length=length)
    for ingredient in ingredients:
        pos = dsp.rand(0, length-ingredient.dur)
        out.dub(ingredient, pos)

    out = fx.norm(out, 0.5)

    return out

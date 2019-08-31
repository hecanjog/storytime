from storytime import farm, prep, bake

if __name__ == '__main__':
    length = 90

    crops = farm.harvest(3, None)
    ingredients = []
    for crop in crops:
        ingredients += [ prep.one(None, crop) ]
    
    out = bake.mix(ingredients, length)

    out.write('baked.wav')

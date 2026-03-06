import random

def weighted_srs(data, n, weights, with_replacement):
    sample = []
    for _ in range(n):
        choice = random.choices(data, weights=weights)[0]
        sample.append(choice)
        if not with_replacement:
            i = data.index(choice)
            data.pop(i)
            weights.pop(i)
    return sample

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()


def get_belt(user_score, scores=scores, belts=belts):
    if user_score < scores[0]:
        return None
    elif scores[-1] <= user_score:
        return belts[-1]

    for idx, (upper, lower) in enumerate(zip(scores[1:], scores)):
        if lower <= user_score < upper:
            return belts[idx]


if __name__ == "__main__":
    print(get_belt(5))
    print(get_belt(800))
    print(get_belt(150))
    print(get_belt(1000))
    print(get_belt(1e6))

#Pizza.py

DELUXE = {
    "Cheese": 100,
    "BaconHam": 120,
    "OnionsChili": 110,
}

SPECIAL = {
    "Cheese": 100,
    "Pepper": 80,
    "BaconHam": 120,
    "Mushroom": 130,
    "OnionsChili": 110
}

PRIMO = {
    "MozzarellaCheese": 150,
    "Pepper": 80,
    "BaconHam": 120,
    "Mushroom": 130,
    "OnionsChili": 110,
    "Tomato": 90,
    "Pineapple": 100,
    "Salami": 120,
}


def deluxe():
    total = sum(DELUXE.values())
    return total

def special():
    total = sum(SPECIAL.values())
    return total

def primo():
    total = sum(PRIMO.values())
    return total


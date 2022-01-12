import random
import os, time, sys

wild_adventures = [
    "Exchange spirit animal tramp stamps",
    "Offer up origami sacrifices to the fire gods",
    "Bond over our mutual love of football",
    "24 hours straight of wild sex",
    "Share our personal interpretations of the snow dance",
    "Find Jesus at Al Green's church",
    "Wing it",
    "Teach Robbie how to use a sewing machine",
    "Teach Ali how to code",
    "Be a tourist in your own city (Go find Elvis' ghost at Graceland)",
    "Be a tourist in your own city (Get sloppy and dance to blues on Beale)",
    "Be a tourist in your own city (Let your soul die at the Bass Pro Pyramid)",
    "Volunteer at a soup drive/kitchen",
    "Bike the green line",
    "Get drunk, create the ultimate dance playlist, and do a home disco",
    "Eat a deep fried twinkie at Dyer's",
    "Eat a soul burger at Ernstein & Hazel's",
    "Get spoopy at a ghost tour",
    "Get all the fabrics at Joann's",
    "Pick a theme/movie, cook a meal and make some cocktails to match",
]

def build_suspense(idea_that_takes_no_time_load):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n\n\n\n\n\n\n\n\n")

    party_time = u"\U0001F38A"

    moons = [
        u"\U0001F311", 
        u"\U0001F312", 
        u"\U0001F313", 
        u"\U0001F314",
        u"\U0001F315",
        u"\U0001F316",
        u"\U0001F317",
        u"\U0001F318"]

    for i in range(21):
        time.sleep(0.2)
        sys.stdout.write("\r" + moons[i % len(moons)].center(90))
        sys.stdout.flush()
    print("\n\n\n\n\n")
    print(f"{party_time} {idea_that_takes_no_time_load} {party_time}".center(90))
    print("\n\n\n\n\n")

build_suspense(random.choice(wild_adventures))
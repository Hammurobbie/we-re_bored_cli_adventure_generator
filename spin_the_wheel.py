import random
import os, time, sys

wild_adventures = [
    "Exchange spirit animal tramp stamps",
    "Offer up origami sacrifices to the fire gods",
    "Bond over our mutual love of football",
    "24 hours straight of wild sex",
    "Share our personal interpretations of the snow dance",
    "Find Jesus at Al Green's church",
    "Idk you're on your own",
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
    "Find a tapestry to crossstitch",
    "Watch Virgina Wolfe (possibly with a drinking game)",
    "(If you're in a season) go look at something seasonal",
    "Make a biblically accurate Mofongo",
    "Repot the plants",
    "Frame and hang polaroids",
    "Check out a new restaurant/bar",
    "Watch a movie from the watch list",
    "Go play games (arcade, mini golf, frisbee etc.)",
    "Find a dumb photoshoot like Sear's or somethin",
]


def build_suspense(idea_that_takes_no_time_load):
    os.system("cls" if os.name == "nt" else "clear")

    party_time = "\U0001F38A"

    moons = [
        "\U0001F311",
        "\U0001F312",
        "\U0001F313",
        "\U0001F314",
        "\U0001F315",
        "\U0001F316",
        "\U0001F317",
        "\U0001F318",
    ]

    terminal_size = os.get_terminal_size()

    print("\n" * int(int(terminal_size.lines) / 2 - 2))
    for i in range(21):
        time.sleep(0.2)
        sys.stdout.write("\r" + moons[i % len(moons)].center(terminal_size.columns - 2))
        sys.stdout.flush()
    print("\n\n\n\n")
    print(
        f"{party_time} {idea_that_takes_no_time_load} {party_time}".center(
            terminal_size.columns - 2
        )
    )
    print("\n" * int(int(terminal_size.lines) * 0.25))


build_suspense(random.choice(wild_adventures))

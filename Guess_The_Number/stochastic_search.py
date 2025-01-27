import random as rd


def init_random_nbr(game_nb: dict) -> int:
    random_nb = rd.randint(game_nb["min"], game_nb["max"])
    return random_nb


def guessing_the_number(game_nb: dict) -> None:
    while game_nb["user_nb"] != game_nb["random_nb"]:
        game_nb["number_of_try"] += 1
        if game_nb["user_nb"] > game_nb["random_nb"]:
            game_nb["max"] = game_nb["user_nb"] - 1
            game_nb["user_nb"] = init_random_nbr(game_nb)
        elif game_nb["user_nb"] < game_nb["random_nb"]:
            game_nb["min"] = game_nb["user_nb"] + 1
            game_nb["user_nb"] = init_random_nbr(game_nb)
    return


def stochastic_method() -> list:
    lst = []
    for i in range(10001):
        game_nb = {"random_nb": 0, "user_nb": 0,
                   "number_of_try": 1,
                   "min": 1, "max": 100}
        game_nb["random_nb"] = init_random_nbr(game_nb)
        game_nb["user_nb"] = init_random_nbr(game_nb)
        guessing_the_number(game_nb)
        lst.append(game_nb["number_of_try"])
    return lst


def main():
    lst = stochastic_method()
    print(f"The average number of guesses per game is {sum(lst) / len(lst):.2f}.")


if __name__ == "__main__":
    main()

import random as rd


def check_number(user_input: str) -> bool:
    try:
        int(user_input)
    except Exception:
        return True


def init_random_user() -> int:
    random_nb = rd.randint(1, 100)
    return random_nb


def init_input_user() -> int:
    input_user = input("Pick a number between 1 and 100. Let's see if you can guess it!\n - ")
    while check_number(input_user):
        input_user = input("Choose a number from 1 to 100. Spoiler: it's not 101 or -1!\n - ")
    return int(input_user)


def guessing_the_number(game_nb: dict) -> None:
    while game_nb["user_nb"] != game_nb["random_nb"]:
        game_nb["number_of_try"] += 1
        if game_nb["user_nb"] > game_nb["random_nb"]:
            print("Your guess is too high! Try a lower number.\n")
            game_nb["user_nb"] = init_input_user()
        elif game_nb["user_nb"] < game_nb["random_nb"]:
            print("Your guess is too low! Try a higher number.\n")
            game_nb["user_nb"] = init_input_user()
    print("Congratulations! You guessed the number! 🎉 You're a true number wizard!")
    return


def main():
    game_nb = {"random_nb": 0,
               "user_nb": 0,
               "number_of_try": 1}
    game_nb["random_nb"] = init_random_user()
    game_nb["user_nb"] = init_input_user()
    guessing_the_number(game_nb)
    return


if __name__ == "__main__":
    main()

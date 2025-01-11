import random as rd


def show_an_empty_one(gate_state, player_state, user_gate):
    if player_state[user_gate]:
        first_gate_to_show = next(iter(gate_state))
        gate_state.pop(first_gate_to_show)
        return
    else:
        for i in gate_state:
            if not gate_state[i]:
                gate_state.pop(i)
                return


def show_the_results(gate_state, player_state, user_gate, ask, stats):
    if ask == "Y":
        other_gate = next(iter(gate_state))
        if gate_state[other_gate]:
            stats["win"] += 1
        else:
            stats["loose"] += 1
    else:
        if player_state[user_gate]:
            stats["win"] += 1
        else:
            stats["loose"] += 1


def random_gift(dic):
    gate, gift = rd.choice(list(dic.items()))
    dic[gate] = True
    return


def random_choice_of_gate(gate_state, player_state):
    gate, gift = rd.choice(list(gate_state.items()))
    player_state[gate] = gift
    gate_state.pop(gate)
    return gate


def parse_input(number_of_game):
    try:
        int(number_of_game)
    except ValueError:
        return True
    return False


def main():
    stats = {"game": 0, "win": 0, "loose": 0}
    number_of_game = input("Choose the number of games: \n")
    while parse_input(number_of_game):
        number_of_game = input("Choose a number of game: \n")
    ask = input("Do you always want to switch if you can? [Y/N] ")
    while ask != "Y" and ask != "N":
        ask = input("Do you always want to switch if you can? [Y/N] ")

    for i in range(int(number_of_game)):
        stats["game"] += 1
        gate_state = {"A": False, "B": False, "C": False}
        player_state = {}
        random_gift(gate_state)
        user_gate = random_choice_of_gate(gate_state, player_state)
        show_an_empty_one(gate_state, player_state, user_gate)
        show_the_results(gate_state, player_state, user_gate, ask, stats)
    print(f"Simulation complete: Out of {stats["game"]} games"
          f"there were {stats["win"]} wins"
          f"({(stats["win"]/stats["game"] * 100):.2f}%) and {stats["loose"]}"
          f"looses ({(stats["loose"]/stats["game"] * 100):.2f}%).")


if __name__ == "__main__":
    main()

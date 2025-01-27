from binary_search import binary_method
from stochastic_search import stochastic_method


def main():
    lst_binary = binary_method()
    lst_stochastic = stochastic_method()

    print(f"Binary search nailed it with an average of {sum(lst_binary) / len(lst_binary):.2f} guesses per game,"
      f"while the stochastic method rocked it with {sum(lst_stochastic) / len(lst_stochastic):.2f} guesses! 🚀")
    return 


if __name__ == "__main__":
    main()

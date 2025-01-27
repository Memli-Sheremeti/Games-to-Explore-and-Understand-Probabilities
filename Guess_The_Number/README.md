# Guess the Number

Welcome to the **Guess the Number** directory! This section contains the implementation of a classic number guessing game with various strategies to explore and compare their efficiency.

---

## 🎯 **Purpose**
The purpose of this game is to:
- Experiment with random number generation.
- Compare search strategies such as binary search and stochastic methods.
- Allow users to play an interactive number guessing game.

---

## 📚 **Contents**
This directory includes the following files:

### 1. **`__main__.py`**
- The main file to run the game.
- Compares the efficiency of binary search and stochastic search methods over multiple iterations.

### 2. **`binary_search.py`**
- Implements the binary search strategy for guessing the number.
- The computer narrows down guesses by halving the search range at each step.

### 3. **`stochastic_search.py`**
- Implements the stochastic search strategy for guessing the number.
- The computer makes random guesses within the valid range until it finds the correct number.

### 4. **`user_test_game.py`**
- An interactive game where the user guesses the number chosen randomly by the computer.
- Provides feedback ("too high" or "too low") after each guess until the correct number is found.

---

## 🚀 **How to Run**

### Prerequisites
- Python 3.x installed on your system.

### Running the Game

#### Run All Strategies and Compare Results
1. Navigate to the `Guess_The_Number/` directory:
   ```bash
   cd Guess_The_Number
   ```
2. Execute the main file:
   ```bash
   python __main__.py
   ```

#### Run Individual Strategies
- **Binary Search:**
  ```bash
  python binary_search.py
  ```
- **Stochastic Search:**
  ```bash
  python stochastic_search.py
  ```

#### Play the Interactive Game
1. Run the interactive game:
   ```bash
   python user_test_game.py
   ```
2. Follow the prompts to guess the number chosen by the computer.

---

## 🛠️ **Future Enhancements**
Here are some potential improvements for this directory:
- **Dynamic Range:** Allow users to customize the range of numbers.
- **Visualization:** Add visualizations to show the efficiency of different strategies.
- **Difficulty Levels:** Introduce different difficulty levels with varied ranges or constraints.

---

## 🤝 **Contributions**
Contributions are welcome! If you have ideas for new strategies or improvements, feel free to open an issue or submit a pull request.

### Guidelines
- Follow Python best practices (PEP 8).
- Include clear documentation and comments for your code.

---

## 📜 **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Happy guessing and exploring search strategies! 🎯✨

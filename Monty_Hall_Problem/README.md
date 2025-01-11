# Monty Hall Problem Simulation

## 🎯 **Overview**
This project simulates the famous Monty Hall problem, a probability puzzle based on a game show scenario. The simulation allows users to explore its counterintuitive solution by running multiple iterations of the game to analyze the probabilities.

---

## 📚 **What is the Monty Hall Problem?**
The Monty Hall problem is a probability puzzle based on the following scenario:

1. **Three Doors:** You are presented with three doors.
   - Behind one door is a car (the prize).
   - Behind the other two doors are goats.

2. **Host's Action:** The host, who knows what’s behind each door, opens one of the two doors you didn't choose to reveal a goat.

3. **The Dilemma:** In a typical version of the game, the player can either:
   - **Stick** with their original choice, or
   - **Switch** to the other unopened door.

4. **The Question:** Does switching increase your chances of winning the car?

---

## 💻 **Features**
- **Simulations Only:** Run a specified number of games (`N`) to analyze the probabilities of winning by sticking versus switching.
- **Automated Gameplay:** The player cannot choose a door manually; the simulation handles all decisions to maximize statistical accuracy.
- **Visualization:** See aggregate results of "stick" vs "switch" strategies over multiple games.

---

## 🚀 **How to Run the Simulation**

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:Memli-Sheremeti/Games-to-Explore-and-Understand-Probabilities.git
   cd Monty_Hall_Problem
   ```

2. **Set Up the Environment**:
   - Ensure Python 3.x is installed.
   - Install any required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Simulation**:
   ```bash
   python monty_hall.py.py
   ```

---

## 📊 **Results and Insights**
- **Switching Strategy:** Increases your chances of winning the car to approximately **66.7%**.
- **Sticking Strategy:** Keeps your chances at **33.3%**.
- The simulation confirms the counterintuitive nature of the problem and highlights the importance of probability in decision-making.

---

## 🤝 **Contributions**
Contributions are welcome! Feel free to:
- Submit issues for bugs or feature requests.
- Open pull requests with improvements or new features.

### Guidelines:
- Ensure your code follows Python best practices (PEP 8).
- Include comments and documentation for your changes.

---

## 📜 **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💡 **Feedback**
If you have any suggestions or questions, feel free to reach out or open an issue. Let's explore the Monty Hall problem together and uncover the magic of probabilities! 🚪🚗🐐

---

Happy coding and learning! 🎲

# 🐦 Buggy Bird Game Extension for Burp Suite

Welcome to the Buggy Bird Game! This Burp Suite extension introduces a fun mini-game reminiscent of the classic "Flappy Bird" directly into your Burp Suite tool. Test your reflexes and enjoy some downtime while working on your security assessments.

## 📋 Features

- 🐤 **Flappy Bird-like Gameplay**: Control the bird and navigate through firewalls.
- ⛔ **Dynamic Obstacles**: Firewalls with varying heights and gaps.
- 🎮 **Score Tracking**: Keeps track of your current and high scores.
- 🎨 **Stylish Design**: Matrix-inspired background and neon colors.

## 📦 Installation

1. **Download the Extension**: Clone or download this repository to your local machine.
2. **Load into Burp Suite**:
   - Open Burp Suite.
   - Go to the "Extender" tab.
   - Click on "Add" and select the `BuggyBirdExtension.py` file.
3. **Start Playing**: Navigate to the "Buggy Bird" tab in Burp Suite to start the game.

## 🚀 How to Play

1. **Start the Game**: Press `SPACE` to start the game.
2. **Control the Bird**: Use `SPACE` to make the bird jump.
3. **Avoid Firewalls**: Navigate through the gaps in the firewalls.
4. **Score Points**: Pass through firewalls to increase your score.
5. **Game Over**: If you hit a firewall or the ground, the game will end. Press `SPACE` to restart.

## 🛠️ Code Overview

### `BuggyBirdPanel`
- **Initialization**: Sets up game parameters, key listeners, and the game timer.
- **Game Mechanics**: Handles bird movement, firewall generation, collision detection, and scoring.
- **Rendering**: Draws the bird, firewalls, and game UI elements.

## 🖼️ Screenshot

![image](https://github.com/user-attachments/assets/18717adc-90dc-4ec9-b7d0-20db63aef509)



## 📝 License

This project is licensed under the MIT License.

---

Enjoy playing Buggy Bird while enhancing your security skills with Burp Suite! If you encounter any issues or have suggestions, feel free to open an issue or contact us.

Happy Hacking! 🚀

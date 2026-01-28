# 🪓 Lumberjack's Profit - Market Simulator

A strategy-based economic simulation where you manage a logging business over a 10-day period. The goal is simple: buy low (with your time) and sell high. Since the market price of wood fluctuates daily, you must decide whether to stockpile your inventory or cash out for a profit.

This project focuses on teaching:
* **Dynamic Variable Scaling:** Changing game values (prices) every iteration of a loop.
* **Accumulator Logic:** Managing a persistent "Inventory" and "Cash" balance.
* **Resource Valuation:** Calculating total earnings based on `quantity * current_price`.
* **Turn-Based Systems:** Using a loop counter to represent a calendar or timeline.

---

## ✨ Features

* **Fluctuating Market:** Prices change randomly between $5 and $20 every single day.
* **Work vs. Trade Mechanics:** Choose to chop wood (increase inventory) or sell wood (increase cash).
* **Randomized Labor:** Chopping wood yields a random amount of logs, simulating varying daily productivity.
* **Score Summary:** A final earnings report is generated at the end of the 10-day cycle.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `lumberjack.py`.
2.  **Open Terminal:** Navigate to the folder where you saved the file.
3.  **Run the Script:**
    ```bash
    python lumberjack.py
    ```

### 3. Gameplay Instructions
1.  **Check the Price:** Look at today's wood price.
2.  **Choose an Action:**
    * **[C]hop:** Spend the day working to add 2-5 logs to your inventory.
    * **[S]ell:** Trade all current inventory for the current market price.
    * **[W]ait:** Do nothing and see if the price goes up tomorrow.
3.  **Maximize Profit:** Try to time your sales when the price is near $20!



---

## 🧠 Code Structure Highlights

### The Market Engine
The "Economic Engine" lives at the start of the loop. Every "Day" (loop iteration) triggers a new price generation, forcing the player to adapt:
```python
market_price = random.randint(5, 20)


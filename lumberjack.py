import random

def lumberjack_tycoon():
    # 1. Game Setup
    money = 0
    wood_inventory = 0
    day = 1
    max_days = 10

    print("--- 🪓 Lumberjack's Profit 🪓 ---")
    print("Goal: Make as much money as possible in 10 days!")

    while day <= max_days:
        # 2. Dynamic Market Price (Price fluctuates between $5 and $20)
        market_price = random.randint(5, 20)
        
        print(f"\n--- Day {day} of {max_days} ---")
        print(f"Current Wood Price: ${market_price} per log")
        print(f"Inventory: {wood_inventory} logs | Cash: ${money}")
        
        action = input("Choose: [C]hop Wood, [S]ell All, [W]ait: ").lower().strip()

        # 3. Game Logic
        if action == 'c':
            logs_chopped = random.randint(2, 5)
            wood_inventory += logs_chopped
            print(f"🪓 You spent the day chopping and got {logs_chopped} logs.")
        
        elif action == 's':
            if wood_inventory > 0:
                earnings = wood_inventory * market_price
                money += earnings
                print(f"💰 Sold {wood_inventory} logs for ${earnings}!")
                wood_inventory = 0
            else:
                print("❌ You have no wood to sell!")
        
        elif action == 'w':
            print("😴 You rested today, hoping for better prices tomorrow.")
        
        else:
            print("❓ Invalid action. You wasted the day!")

        day += 1

    # 4. Final Score
    print("\n" + "="*20)
    print(f"GAME OVER! Total Profit: ${money}")
    print("="*20)

lumberjack_tycoon()

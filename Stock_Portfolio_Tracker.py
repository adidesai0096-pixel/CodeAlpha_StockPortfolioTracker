import json
import os

FILE_NAME = "portfolio.json"


def load_portfolio():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not load saved portfolio.")
    return {}


def save_portfolio(portfolio):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(portfolio, file, indent=4)
    except OSError:
        print("Error: Could not save portfolio.")


def add_stock(portfolio):
    name = input("Enter stock name or symbol: ").strip().upper()

    if not name:
        print("Stock name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        purchase_price = float(input("Enter purchase price per share: "))

        if quantity <= 0 or purchase_price <= 0:
            print("Quantity and price must be greater than zero.")
            return

        if name in portfolio:
            old_stock = portfolio[name]
            old_quantity = old_stock["quantity"]
            total_quantity = old_quantity + quantity

            old_cost = old_quantity * old_stock["purchase_price"]
            new_cost = quantity * purchase_price

            average_price = (old_cost + new_cost) / total_quantity

            portfolio[name]["quantity"] = total_quantity
            portfolio[name]["purchase_price"] = round(average_price, 2)
        else:
            portfolio[name] = {
                "quantity": quantity,
                "purchase_price": round(purchase_price, 2)
            }

        save_portfolio(portfolio)
        print(f"{name} added successfully!")

    except ValueError:
        print("Please enter a valid quantity and price.")


def view_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\n" + "=" * 65)
    print(f"{'STOCK':<15}{'QUANTITY':<12}{'BUY PRICE':<15}{'INVESTMENT':<15}")
    print("=" * 65)

    total_investment = 0

    for name, details in portfolio.items():
        quantity = details["quantity"]
        purchase_price = details["purchase_price"]
        investment = quantity * purchase_price
        total_investment += investment

        print(
            f"{name:<15}{quantity:<12}"
            f"₹{purchase_price:<14.2f}₹{investment:.2f}"
        )

    print("=" * 65)
    print(f"Total investment: ₹{total_investment:.2f}")


def calculate_profit_loss(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    name = input("Enter stock symbol: ").strip().upper()

    if name not in portfolio:
        print("Stock not found in your portfolio.")
        return

    try:
        current_price = float(input("Enter current price per share: "))

        if current_price < 0:
            print("Current price cannot be negative.")
            return

        stock = portfolio[name]
        quantity = stock["quantity"]
        purchase_price = stock["purchase_price"]

        investment = quantity * purchase_price
        current_value = quantity * current_price
        profit_loss = current_value - investment

        print(f"\nStock: {name}")
        print(f"Original investment: ₹{investment:.2f}")
        print(f"Current value: ₹{current_value:.2f}")

        if profit_loss > 0:
            print(f"Profit: ₹{profit_loss:.2f}")
        elif profit_loss < 0:
            print(f"Loss: ₹{abs(profit_loss):.2f}")
        else:
            print("No profit or loss.")

    except ValueError:
        print("Please enter a valid price.")


def remove_stock(portfolio):
    name = input("Enter stock symbol to remove: ").strip().upper()

    if name in portfolio:
        del portfolio[name]
        save_portfolio(portfolio)
        print(f"{name} removed successfully!")
    else:
        print("Stock not found in your portfolio.")


def main():
    portfolio = load_portfolio()

    while True:
        print("\n========== STOCK PORTFOLIO TRACKER ==========")
        print("1. Add stock")
        print("2. View portfolio")
        print("3. Calculate profit or loss")
        print("4. Remove stock")
        print("5. Exit")
        print("=============================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_stock(portfolio)
        elif choice == "2":
            view_portfolio(portfolio)
        elif choice == "3":
            calculate_profit_loss(portfolio)
        elif choice == "4":
            remove_stock(portfolio)
        elif choice == "5":
            save_portfolio(portfolio)
            print("Portfolio saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
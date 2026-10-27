📈 Stock Portfolio Tracker

📌 Project Overview

The Stock Portfolio Tracker is a Python-based application developed as part of the CodeAlpha Python Programming Internship.

This application helps users manage their stock investments by allowing them to add stocks, view their portfolio, calculate total investment, and determine potential profit or loss using manually entered stock prices.

The project demonstrates fundamental Python programming concepts, including functions, dictionaries, conditional statements, exception handling, and JSON file handling.

🎯 Objectives

- Develop a simple stock portfolio management application using Python.
- Allow users to record stock purchases and quantities.
- Calculate the total amount invested in stocks.
- Calculate potential profit or loss using a manually entered current price.
- Store portfolio information so it remains available between program sessions.

✨ Features

- Add Stocks: Enter a stock symbol, quantity, and purchase price.
- View Portfolio: Display stock holdings, quantities, purchase prices, and investment amounts.
- Calculate Profit or Loss: Calculate the difference between the purchase cost and current value.
- Remove Stocks: Remove a stock from the portfolio.
- Data Persistence: Save and load portfolio information using a JSON file.
- Input Validation: Handle invalid quantities, prices, and menu choices.
- Average Purchase Price: Update the average purchase price when additional shares of an existing stock are added.

🛠️ Technologies Used

- Programming Language: Python
- Code Editor: Visual Studio Code
- Data Storage: JSON
- Python Modules: "json", "os"

💻 Requirements

- Python 3 installed on your computer.
- Visual Studio Code or another Python-compatible editor.
- A terminal or command prompt.

No external Python packages are required.

🚀 How to Run the Project

Step 1: Download the Repository

Clone the repository using:

git clone https://github.com/adidesai0096-pixel/CodeAlpha_StockPortfolioTracker.git

Alternatively, download the repository as a ZIP file from GitHub and extract it.

Step 2: Open the Project

Open the project folder in Visual Studio Code.

Step 3: Run the Program

Open the terminal in the project folder and execute:

python Stock_Portfolio_Tracker.py

If the command above does not work on Windows, try:

py Stock_Portfolio_Tracker.py

Step 4: Use the Menu

The application provides the following options:

1. Add Stock
2. View Portfolio
3. Calculate Profit or Loss
4. Remove Stock
5. Exit

Choose an option and follow the instructions displayed in the terminal.

🧮 Example Calculation

Suppose a user purchases 10 shares of TCS at ₹3,500 per share.

- Quantity: 10 shares
- Purchase price per share: ₹3,500
- Total investment: ₹35,000
- Sample current price per share: ₹3,700
- Current portfolio value: ₹37,000
- Calculated profit: ₹2,000

Formula:

Total Investment = Quantity × Purchase Price

Current Value = Quantity × Current Price

Profit or Loss = Current Value − Total Investment

The prices above are illustrative examples, not live market prices.

📂 Project Structure

CodeAlpha_StockPortfolioTracker/
│
├── Stock_Portfolio_Tracker.py
├── README_Stock_Portfolio.md
└── portfolio.json  (created when portfolio data is saved)

The "portfolio.json" file stores the portfolio data locally. It is generated when the program saves the portfolio.

📚 Python Concepts Demonstrated

- Functions and modular programming
- Dictionaries and data structures
- Loops and conditional statements
- User input and output
- Exception handling
- File handling
- JSON serialization and deserialization
- Basic financial calculations

🔮 Future Enhancements

- Integrate a reliable stock market API for live prices.
- Add graphical charts showing portfolio performance.
- Support multiple portfolios.
- Export portfolio reports to CSV or Excel.
- Add a graphical user interface.

⚠️ Disclaimer

This project is intended for educational purposes only. Stock prices are entered manually and are not retrieved from a live market data service. Calculations are estimates based on the values entered by the user. This application does not provide financial or investment advice.

👨‍💻 Author

Aditya Desai

Developed as part of the CodeAlpha Python Programming Internship – Task 2.

🔗 GitHub Repository

https://github.com/adidesai0096-pixel/CodeAlpha_StockPortfolioTracker

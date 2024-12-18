### main.py
# This section is for the main application logic
from functions import (
    register_user,
    authenticate_user,
    get_closing_prices,
    analyze_closing_prices,
    save_to_csv,
    read_from_csv,
)

def main():
    print("Welcome to the Stock Selection Tool!")

    # User Registration and Authentication
    logged_in = False
    while not logged_in:
        action = input("Choose an option: Register (R) / Login (L): ").strip().upper()
        if action == "R":
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            if register_user(email, password):
                print("Registration successful! You can now log in.")
            else:
                print("Registration failed. Try again.")
        elif action == "L":
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            if authenticate_user(email, password):
                print("Login successful!")
                logged_in = True
            else:
                print("Invalid email or password. Try again.")
        else:
            print("Invalid choice. Please type 'R' to Register or 'L' to Login.")

    # Stock Data Retrieval and Analysis
    while True:
        ticker = input("Enter stock ticker (e.g., AAPL, TSLA): ").strip()
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        end_date = input("End date (YYYY-MM-DD): ").strip()

        prices = get_closing_prices(ticker, start_date, end_date)
        if prices is not None and not prices.empty:
            analysis = analyze_closing_prices(prices)

            print("\n--- Analysis Summary ---")
            for key, value in analysis.items():
                print(f"{key}: {value}")

            save_to_csv({"email": email, "ticker": ticker, **analysis}, "user_data.csv")

            if input("View saved data? (y/n): ").strip().lower() == 'y':
                read_from_csv("user_data.csv")
        else:
            print("Error retrieving stock data. Please check your inputs.")

        if input("Analyze another stock? (y/n): ").strip().lower() != 'y':
            print("Thank you for using the Stock Selection Tool! Goodbye.")
            break

if __name__ == "__main__":
    main()

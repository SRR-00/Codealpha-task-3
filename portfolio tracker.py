import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol] -= quantity

    def portfolio_value(self):
        total_value = 0.0
        for symbol, quantity in self.portfolio.items():
            stock = yf.Ticker(symbol + ".NS")  # Append ".NS" for stocks listed on NSE (Indian stock exchange)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            total_value += current_price * quantity
        return total_value

    def track_performance(self):
        print("Current Portfolio:")
        for symbol, quantity in self.portfolio.items():
            stock = yf.Ticker(symbol + ".NS")  # Append ".NS" for stocks listed on NSE (Indian stock exchange)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            print(f"{symbol}: Quantity - {quantity}, Current Price - {current_price}")

if __name__ == "__main__":
    portfolio = StockPortfolio()

    # Input from user
    while True:
        symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
        if symbol == "":
            break
        try:
            quantity = float(input(f"Enter quantity of {symbol}: "))
            portfolio.add_stock(symbol, quantity)
        except ValueError:
            print("Invalid quantity! Please enter a valid number.")

    portfolio.track_performance()

    # Checking total portfolio value
    try:
        print(f"Total Portfolio Value: ₹{portfolio.portfolio_value():,.2f}")
    except Exception as e:
        print("Error calculating portfolio value:", e)

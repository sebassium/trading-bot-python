class Portfolio():

    def __init__(self):
        self.positions = {}

    def add_position(self, symbol: str, quantity: int) -> dict:

        self.positions[symbol] = {}
        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['quantity'] = quantity

        return self.positions


p1 = Portfolio()
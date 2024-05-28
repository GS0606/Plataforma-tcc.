

class Currency:
    def __init__(self, base_currency, target_currency, rate):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.rate = rate

    def to_dict(self):
        return {
            "base_currency": self.base_currency,
            "target_currency": self.target_currency,
            "rate": self.rate
        }

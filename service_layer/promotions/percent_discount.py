"""The PercentDiscount Module."""
from models import PromotionModel


class PercentDiscount(PromotionModel):
    """Applies a percentage discount to all items."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_discount(self, price: (int, float), quantity: (int, float)):
        """Overriding Method to Apply percentage discount."""
        return price * quantity * (1 - self.percent / 100)

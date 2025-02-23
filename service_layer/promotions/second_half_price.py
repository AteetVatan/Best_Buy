"""The SecondHalfPrice Module"""
from models import PromotionModel


class SecondHalfPrice(PromotionModel):
    """Applies a 50% discount on every second item."""

    def apply_discount(self, price: (int, float), quantity: (int, float)):
        """Overriding Method to Calculate Discount for every Second item."""
        if quantity < 2:
            return price * quantity
        discounted_items = quantity // 2
        full_price_items = quantity - discounted_items
        return (full_price_items * price) + (discounted_items * price * 0.5)

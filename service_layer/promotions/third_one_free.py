"""The ThirdOneFree Module."""
from models import PromotionModel


class ThirdOneFree(PromotionModel):
    """Every third item is free."""

    def apply_discount(self, price: (int, float), quantity: (int, float)):
        """Makes all Third Items Free."""
        free_items = quantity // 3
        payable_items = quantity - free_items
        return payable_items * price

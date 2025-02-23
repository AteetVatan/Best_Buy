"""The Non StockProduct Module"""
from typing import Tuple

from constants import ConstantStrings
from helpers import UserText
from models.product_model import ProductModel


class LimitedProduct(ProductModel):
    """The Non StockProduct Class"""

    def buy(self, buy_quantity: (int, float)) -> Tuple[float, str]:
        """Method to buy the product.
        :param buy_quantity: The Product Quantity.
        :return: (price, applied_promotion_name) of type Tuple[float, str].
        """
        try:
            self.buy_validation(buy_quantity)
            # price = self.get_best_price(buy_quantity)
            price_promotion_tuple = self.get_best_price(buy_quantity)
            self.quantity -= buy_quantity
            return price_promotion_tuple
        except ValueError as e:
            UserText.print_error(ConstantStrings.
                                 EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

    def buy_validation(self, buy_quantity: (int, float)):
        """Method to Validate the Buy Quantity"""
        if self.quantity == 0:
            raise ValueError(ConstantStrings.PRODUCT_QUANTITY_EMPTY_ERROR)
        # Quantity Validation
        buy_quantity = ProductModel.validate_quantity(buy_quantity)

        if buy_quantity == 0:
            # Nothing was Bought
            raise ValueError(ConstantStrings.PRODUCT_BUY_QUANTITY_ERROR)
        if buy_quantity > self.maximum:
            # buy_quantity is greater than maximum shippable quantity size
            raise ValueError(ConstantStrings.PRODUCT_QUANTITY_EXCEED_MAXIMUM)
        if buy_quantity > self.quantity:
            # buy_quantity is greater than product quantity
            raise ValueError(ConstantStrings.PRODUCT_QUANTITY_NOT_AVAILABLE)

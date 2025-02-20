"""The Non StockProduct Module"""
from constants import ConstantStrings
from models.product_model import ProductModel


class LimitedProduct(ProductModel):
    """The Non StockProduct Class"""
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity, maximum)

    def buy(self, buy_quantity: (int, float)) -> float:
        """Method to buy the product"""
        try:
            self.buy_validation(buy_quantity)
            self.quantity -= buy_quantity
            return self.price * buy_quantity
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="quantity", exception=e))
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
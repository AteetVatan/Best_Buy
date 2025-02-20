"""The Non StockProduct Module"""
from constants import ConstantStrings
from models.product_model import ProductModel


class NonStockedProduct(ProductModel):
    """The Non StockProduct Class"""
    def __init__(self, name: str, price: (int, float)):
        super().__init__(name, price)

    def buy(self, buy_quantity: (int, float)) -> float:
        """Method to buy the product"""
        try:
            self.buy_validation(buy_quantity)
            return self.price * buy_quantity
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

    def buy_validation(self, buy_quantity: (int, float)):
        """Method to Validate the Buy Quantity"""
        # Quantity Validation
        buy_quantity = ProductModel.validate_quantity(buy_quantity)

        if buy_quantity == 0:
            # Nothing was Bought
            raise ValueError(ConstantStrings.PRODUCT_BUY_QUANTITY_ERROR)

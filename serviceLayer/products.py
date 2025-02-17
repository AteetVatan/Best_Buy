"""The Main Product Class"""
from models.product_model import ProductModel
from constants import constant


class Product(ProductModel):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def is_active(self) -> None:
        """Return is Product active."""
        return self.active

    def activate(self) -> None:
        """Activates the Product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the Product."""
        self.active = False

    def set_quantity(self, value: (int, float)):
        """Method to set the Product Quantity"""
        self.quantity = value

    def buy(self, quantity: (int, float)) -> float:
        """
        Method to buy the product.
        :param quantity: The product quantity
        :return:  the total price (float) of the purchase.
        """
        try:
            # check quantity is less than existing
            if quantity > self.quantity:
                raise ValueError(constant.PRODUCT_QUANTITY_NOT_AVAILABLE)

            if quantity < 0:
                raise ValueError(constant.PRODUCT_QUANTITY_ERROR)

            self.quantity -= quantity
            return self.price * quantity
        except ValueError as e:
            print(constant.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

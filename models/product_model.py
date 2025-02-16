"""The Product Model Module."""
from constants import constant

class ProductModel:
    """The Product Model Class."""
    __name: str
    __price: float
    __quantity: int
    __active: bool

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__active = True

    @property
    def name(self):
        """Product Name."""
        return self.__name

    @name.setter
    def name(self, value: str):
        try:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(constant.PRODUCT_NAME_ERROR)
            self.__name = value.strip()
        except ValueError as e:
            print(constant.EXCEPTION_STRING.format(field="name",exception=e))
            raise  # re-raises the same exception



    @property
    def price(self):
        """Product Price."""
        return self.__price

    @price.setter
    def price(self, value : (int, float)):
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(constant.PRODUCT_PRICE_ERROR)
            self.__price = value
        except ValueError as e:
            print(constant.EXCEPTION_STRING.format(field="price",exception=e))
            raise

    @property
    def quantity(self):
        """Product Quantity."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: (int, float)):
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(constant.PRODUCT_QUANTITY_ERROR)
            self.__quantity = value
        except ValueError as e:
            print(constant.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

    @property
    def active(self):
        """Is Product Active."""
        return self.__active

    @active.setter
    def active(self, value: bool):
        """Is Product Active."""
        self.__active = value

    def __str__(self):
        """The Product info."""
        return f"Product(name={self.__name}, price={self.__price}, quantity={self.__quantity}, active={self.__active})"



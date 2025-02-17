"""The Product Model Module."""
import uuid
from constants.constant_strings import ConstantStrings


class ProductModel:
    """The Product Model Class."""

    def __init__(self, name, price, quantity):
        self.__name: str = name
        self.__price: float = price
        self.__quantity: int = quantity
        self.__active: bool = True
        self.__id: int = uuid.uuid4().int  # unique id to identify the product

    @property
    def name(self):
        """Product Name."""
        return self.__name

    @name.setter
    def name(self, value: str):
        try:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(ConstantStrings.PRODUCT_NAME_ERROR)
            self.__name = value.strip()
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="name", exception=e))
            raise  # re-raises the same exception

    @property
    def price(self):
        """Product Price."""
        return self.__price

    @price.setter
    def price(self, value: (int, float)):
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(ConstantStrings.PRODUCT_PRICE_ERROR)
            self.__price = value
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="price", exception=e))
            raise

    @property
    def quantity(self):
        """Product Quantity."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: (int, float)):
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(ConstantStrings.PRODUCT_QUANTITY_ERROR)
            self.__quantity = value
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

    @property
    def active(self):
        """Is Product Active."""
        return self.__active

    @active.setter
    def active(self, value: bool):
        """Is Product Active."""
        self.__active = value

    @property
    def id(self):
        """Product Unique ID."""
        return self.__id

    def show(self) -> None:
        """The Product Info"""
        return f"{self.__name}, Price: ${self.__price}, Quantity: {self.__quantity}"

    def __str__(self):
        """The Product info object."""
        return (f"Product(name={self.__name}, "
                f"price={self.__price}, "
                f"quantity={self.__quantity}, "
                f"active={self.__active})")

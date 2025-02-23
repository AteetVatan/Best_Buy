"""The Product Model Module."""
import uuid
from abc import ABC, abstractmethod
from typing import Tuple

from helpers.product_validators import ProductValidators
from models.multiple_promotion_model import MultiplePromotionModel


class ProductModel(ABC, ProductValidators):
    """The Product Model Class."""

    def __init__(self, name, price, quantity=None, maximum=None):
        self.__active = None
        self.__name: str = None
        self.__price: (int, float) = None
        self.__quantity: (int, float) = None
        self.__maximum_order_quantity: (int, float) = None
        # The MultiplePromotionModel Class supporting Multiple Promotions.
        self.__multiple_promotion: MultiplePromotionModel = MultiplePromotionModel()

        self.__active: bool = True  # By default, all products are active.
        self.__id = uuid.uuid4().int  # Unique product id
        self.name, self.price, self.quantity, self.maximum = name, price, quantity, maximum

    @abstractmethod
    def buy(self, buy_quantity: (int, float)) -> Tuple[float, str]:
        """Abstract Method to buy the product.
        :param buy_quantity: The Product Quantity.
        :return: (price, applied_promotion_name) of type Tuple[float, str].
        """
        pass

    @abstractmethod
    def buy_validation(self, buy_quantity: (int, float)):
        """Abstract method to validate buy_quantity."""
        pass

    @property
    def name(self):
        """Product Name."""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Method to validate_and_set_name"""
        self.__name = ProductModel.validate_name(value)

    @property
    def price(self):
        """Product Price."""
        return self.__price

    @price.setter
    def price(self, value: (int, float)):
        """Method to validate_and_set_name"""
        self.__price = ProductModel.validate_price(value)

    @property
    def quantity(self):
        """Product Quantity."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: (int, float)):
        """Product Quantity."""
        if value is not None:
            self.__quantity = ProductModel.validate_quantity(value)
            # if product quantity is zero, deactivate it.
            self.__active = True
            if self.__quantity == 0:
                self.__active = False

    @property
    def maximum(self):
        """Product Maximum Quantity."""
        return self.__maximum_order_quantity

    @maximum.setter
    def maximum(self, value: (int, float)):
        """Product Maximum Quantity."""
        if value is not None:
            self.__maximum_order_quantity = ProductModel.validate_quantity(value)

    @property
    def multiple_promotion(self):
        """Product Maximum Quantity."""
        return self.__multiple_promotion

    @multiple_promotion.setter
    def multiple_promotion(self, input_promotions):
        """Setter to accept a dynamic number of PromotionModel instances."""
        if input_promotions is not None:
            self.__multiple_promotion.promotions = input_promotions  # Convert tuple to list

    @property
    def active(self):
        """Is Product Active."""
        return self.__active

    @active.setter
    def active(self, val: bool):
        """Sets Product Active."""
        self.__active = ProductModel.validate_active(val)

    @property
    def id(self):
        """Product Unique ID."""
        return self.__id

    def get_best_price(self, buy_quantity: (int, float)) -> Tuple[float, str]:
        """
        Method to get the best price available after applying all available promotions.
        :param buy_quantity: The Product Quantity.
        :return: (price, applied_promotion_name) of type Tuple[float, str].
        """
        price = self.price * buy_quantity
        promotion_tuple = None
        if self.__multiple_promotion is not None and len(self.__multiple_promotion) > 0:
            promotion_tuple = self.__multiple_promotion.apply_promotions(
                price=self.price,
                buy_quantity=buy_quantity)

        if promotion_tuple is not None and promotion_tuple[0] < price:
            return promotion_tuple
        return (price,)

    # Region Magic Methods.

    # Use __gt__ (greater than >) and __lt__ (less than <).

    def __gt__(self, other):
        """Greater than - dunder method."""
        return self.price > other.price

    def __lt__(self, other):
        """Less than - dunder method."""
        return self.price < other.price

    def __str__(self) -> str:
        """The Product Info"""
        promotions_str = None
        if self.__multiple_promotion is not None and len(self.__multiple_promotion) > 0:
            promotions_str = " ,".join(x.name for x in self.__multiple_promotion.promotions)

        attributes = {
            "": self.__name,
            "Price: $": self.__price,
            "Quantity: ": self.__quantity,
            "Maximum: ": self.__maximum_order_quantity,
            "Promotions: ": promotions_str
        }
        return ", ".join(f"{k}{v}" for k, v in attributes.items() if v is not None)

    # def __str__(self):
    #     """The Product info object."""
    #     promotions_str = None
    #     if len(self.__multiple_promotion) > 0:
    #         promotions_str = " ,".join(x.name for x in self.__multiple_promotion.promotions)
    #
    #     attributes = {
    #         "name": self.__name,
    #         "price": self.__price,
    #         "quantity": self.__quantity,
    #         "active": self.__active,
    #         "maximum": self.__maximum_order_quantity,
    #         "Promotions: ": promotions_str
    #     }
    #     obj_str = " ,".join(f"{k}={v}" for k, v in attributes.items() if v is not None)
    #     return f"Product({obj_str})"

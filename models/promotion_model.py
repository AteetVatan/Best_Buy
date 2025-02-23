"""The PromotionModel Module."""
from abc import ABC, abstractmethod


class PromotionModel(ABC):
    """Base class for different types of promotions."""

    def __init__(self, name: str):
        self.name = name
        self.__active = True  # By Default, all promotions will be activated

    @abstractmethod
    def apply_discount(self, price: (int, float), quantity: (int, float)):
        """Apply the discount to the given quantity of product."""
        pass

    @property
    def active(self):
        """True when promotion is available."""
        return self.__active

    @active.setter
    def active(self, val: bool):
        """active property setter."""
        self.__active = val

    def __str__(self):
        return self.name

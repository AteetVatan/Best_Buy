"""Module for MultiplePromotionModel."""
from typing import Tuple

from helpers.generic_validator import GenericValidator
from models.promotion_model import PromotionModel


class MultiplePromotionModel:
    """class for MultiplePromotionModel."""

    def __init__(self):
        self.__promotions = []

    def __len__(self):
        """Number of Promotions"""
        return len(self.__promotions)

    @property
    def promotions(self):
        """The promotion list."""
        return self.__promotions

    @promotions.setter
    def promotions(self, input_promotions):
        """Method to add promotion."""
        if not isinstance(input_promotions, tuple):
            input_promotions = (input_promotions,)

        for p in input_promotions:
            GenericValidator.validate_type(p, PromotionModel)

        for p in input_promotions:
            if not p in self.__promotions:
                self.__promotions.append(p)

    def activate_promotion(self, promotion_type: type):
        """Method to activate given promotion."""
        for item in self.__promotions:
            if isinstance(item, promotion_type):
                item.active = True

    def deactivate_all(self):
        """Method to deactivate all promotions."""
        for item in self.__promotions:
            item.active = False

    def apply_promotions(self,
                         price: (int, float),
                         buy_quantity: (int, float)) -> Tuple[float, str]:
        """Method to apply multiple promotions and return the best price and the promotion used.
        :param price: The Product price.
        :param buy_quantity: The Product Quantity.
        :return: (price, applied_promotion_name) of type Tuple[float, str].
        """
        promotion_price_list = []
        for p in (p for p in self.__promotions if p.active):
            promotional_price = p.apply_discount(quantity=buy_quantity, price=price)
            promotion_price_list.append(promotional_price)
        minimum_price = min(promotion_price_list)
        minimum_price_index = promotion_price_list.index(minimum_price)
        applied_promotion_name = str(self.promotions[minimum_price_index])
        return minimum_price, applied_promotion_name

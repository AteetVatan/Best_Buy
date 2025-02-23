"""Module for Generic Validators."""
from constants import ConstantStrings
from helpers.user_text import UserText


class GenericValidator:
    """The GenericValidator class."""

    @staticmethod
    def validate_type(value, class_type: type):
        """Generic Method to validate object Type"""
        try:
            if not isinstance(value, class_type):
                raise TypeError(ConstantStrings.
                                OBJECT_TYPE_ERROR.format(obj_type=class_type.__name__))
            return value
        except TypeError as e:
            UserText.print_error(ConstantStrings.EXCEPTION_STRING.format(field="Type", exception=e))
            raise

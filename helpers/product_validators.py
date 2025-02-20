from constants import ConstantStrings


class ProductValidators:
    """Product Validator Class"""
    @staticmethod
    def validate_name(value: str):
        """Method to validate_and_set_name"""
        try:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(ConstantStrings.PRODUCT_NAME_ERROR)
            return value.strip()
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="name", exception=e))
            raise  # re-raises the same exception

    @staticmethod
    def validate_price(value: (int, float)):
        """Method to validate_and_set_price"""
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(ConstantStrings.PRODUCT_PRICE_ERROR)
            return value
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="price", exception=e))
            raise

    @staticmethod
    def validate_quantity(value: (int, float)):
        """Method to validate_and_set_quantity"""
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(ConstantStrings.PRODUCT_QUANTITY_ERROR)
            return value
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

    @staticmethod
    def validate_maximum_order_quantity(value: (int, float)):
        """Method to validate_maximum_order_quantity."""
        try:
            if not isinstance(value, (int, float)) or value < 0:
                raise ValueError(ConstantStrings.PRODUCT_MAXIMUM_ERROR)
            return value
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise

    @staticmethod
    def validate_active(value: bool):
        """Method to validate_and_set_quantity"""
        try:
            if not isinstance(value,bool):
                raise ValueError(ConstantStrings.PRODUCT_QUANTITY_ERROR)
            return value
        except ValueError as e:
            print(ConstantStrings.EXCEPTION_STRING.format(field="quantity", exception=e))
            raise



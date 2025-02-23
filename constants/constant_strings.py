"""The String Constants Module."""


class ConstantStrings:
    """Class to define String Constants."""
    APP_NAME = "Best Buy"

    PRODUCT_NAME_ERROR = "Name must be a non-empty string."
    PRODUCT_PRICE_ERROR = "Price must be a positive number."
    PRODUCT_QUANTITY_ERROR = "Quantity must be a positive number."
    PRODUCT_QUANTITY_EMPTY_ERROR = "Product is not available."
    PRODUCT_MAXIMUM_ERROR = "Maximum must be a positive number."
    PRODUCT_BUY_QUANTITY_ERROR = "Quantity must be a number greater then Zero."
    PRODUCT_ACTIVE_ERROR = "Active must be a boolean."

    PRODUCT_LIST_HEADER = "---products---"
    PRODUCT_LIST_FOOTER = "-----end------"

    PRODUCT_QUANTITY_NOT_AVAILABLE = "This Quantity is not available."
    PRODUCT_QUANTITY_EXCEED_MAXIMUM = "This Quantity exceeds maximum shippable quantity size."
    PRODUCT_INVALID_TYPE = "Invalid product type."
    STORE_INFO = "Store with {length} products."
    STORE_PRODUCT_NOT_EXISTS = "This product {name} is not in the store."

    EXCEPTION_STRING = "Error setting {field}: {exception}."

    # Menu Strings
    MENU_HEADER = "\n\tStore Menu"
    MENU_OPT_PROMPT = "\nPlease choose a number: "
    MENU_OPT_INVALID = "Error with your choice! Try again!"

    MENU_OPT_1 = "List all products in store"
    MENU_OPT_2 = "Show total amount in store"
    MENU_OPT_3 = "Make an order"
    MENU_OPT_4 = "Quit"

    MENU_TOTAL_QUANTITY = "Total of {number} items in store."

    MAKE_ORDER_ADD_PRODUCT_ERROR = "Error adding product!\n"
    MAKE_ORDER_NO_PRODUCTS = "No products available."
    MAKE_ORDER_FINISH = "\nWhen you want to finish order, [enter an empty text]."
    MAKE_ORDER_PRODUCT_ADDED = "Product added to list!"
    MAKE_ORDER_ADD_PRODUCT = "Which product # do you want? [Enter 1 - {prd_len}]: "
    MAKE_ORDER_ADD_PRODUCT_INDEX_ERROR = "CE-Please enter a product index between 1 - {prd_len}."
    MAKE_ORDER_SELECT_QUANTITY = "What amount do you want? [empty text to order another]: "
    MAKE_ORDER_SELECT_QUANTITY_WITH_MAX = ("What amount do you want? "
                                           "[Maximum Available per order: {max_amt}] \n"
                                           "[empty text to order another]: ")
    MAKE_ORDER_SELECT_QUANTITY_ERROR = ("CE-Quantity larger than the maximum available"
                                        " ({max_amt}).\n")
    MAKE_ORDER_INVALID_QUANTITY = "Quantity should be positive."
    MAKE_ORDER_AMOUNT = "\nOrder made! Total payment: ${total_amt:.2f}"
    MAKE_ORDER_CANCEL = "\nNo product has been added, order cancelled."

    OBJECT_TYPE_ERROR = "The Object Must be of Type {obj_type}"

"""The User Console Text Module."""


class UserText:
    """Class for User Console Texts."""

    @staticmethod
    def print_error(message):
        """Print error messages in red"""
        print("\033[91m" + message + "\033[0m")

    @staticmethod
    def print_success(message):
        """Print output messages in green"""
        print("\033[92m" + message + "\033[0m")

    @staticmethod
    def print_bold(message):
        """Prints text in bold"""
        print("\033[1m" + message + "\033[0m")

    @staticmethod
    def print_teal(message):
        """Prints text in a teal"""
        print("\033[38;5;37m" + message + "\033[0m")

    @staticmethod
    def print_blue(message):
        """Print messages in blue"""
        print("\033[94m" + message + "\033[0m")

    @staticmethod
    def input_prompt(prompt):
        """Print input prompt in a brownish color (yellow)"""
        return input("\033[33m" + prompt + "\033[0m")

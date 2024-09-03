import pyfiglet
from variable import name, font, DEFAULT_START_MESSAGE, bool_info, bool_start_message
from chech import chech_print


def start():
    text = pyfiglet.figlet_format(name, font=font)

    chech_print(bool=bool_start_message, text=text)

    chech_print(bool=bool_info, text=DEFAULT_START_MESSAGE)
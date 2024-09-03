import json_read as json_read
import get_font as get_font

#Main
name = json_read.read_config("name")
version = json_read.read_config("version")

font = get_font.get_font(json_read.read_config("font"))

bool_info = json_read.read_config("bool_info")
bool_start_message = json_read.read_config("bool_start_message")

#Default Message and constants
DEFAULT_START_MESSAGE = f"[INFO]: Name: {name}, Version: {version}"
DEFAULT_ERROR_MESSAGE = "[Error]: Error: "
DEFAULT_FATAL_ERROR_MESSAGE = "[FATAL Error]: Error: "

DEFAULT_WARN_CLOSE_FUNCTION_MESSAGE = "[WARN]: Отказано в доступе. \n[Reason]: возможно отключено в конфиге."
DEFAULT_WARN_MESSAGE = "[WARN]: "

#Debug
Warn = []
Error = []
Fatal_Error = []

bool_work = True
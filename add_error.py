from variable import Fatal_Error, Error, Warn
import Error_print

TYPE_FATAL_ERROR = {}

TYPE_ERROR = {
    1: "Type: Error_Number \n[Number_Error]: 1 \n[Name_Error]: ValueError: could not convert string to int      \n[Reason]: Возникла ошибка, указано некорректное число",
    2: ""
}

TYPE_WARN = {
    1: "Type: Warn_Number \n[Number_Warn]: 1 \n[Reason]: Некоpректый список",
    2: "Type: Warn_Position \n[Number_Warn]: 2 \n[Reason]: Указано некорректная позиция игрока",
    3: "Type: Warn_FullName \n[Number_Warn]: 3 \n[Reason]: Указано некорректное ФИО игрока",
    4: "Type: Warn_Team \n[Number_Warn]: 4 \n[Reason]: Указана некорректная команда для игрока",
    5: "Type: Warn_Date \n[Number_Warn]: 5 \n[Reason]: Указана некорректная дата",
}



def add_fatal_error(Type_Error: int):
    Message = TYPE_FATAL_ERROR[Type_Error]
    Fatal_Error.append(Message)
    Error_print.check_fatal_error()
    

def add_error(Type_Error: int):
    Message = TYPE_ERROR[Type_Error]
    Error.append(Message)
    Error_print.check_error()

def add_warn(Type_Error: int):
    Message = TYPE_WARN[Type_Error]
    Warn.append(Message)
    Error_print.check_warn()

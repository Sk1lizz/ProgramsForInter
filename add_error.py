from variable import Fatal_Error, Error, Warn



TYPE_FATAL_ERROR = {}

TYPE_ERROR = {
    1: "Type: Error_Number \n[Number_Error]: 1 \n[Name_Error]: ValueError: could not convert string to int      \n[Reason]: Возникла ошибка, указано некорректное число",
}

TYPE_WARN = {
    1: "Type: Warn_Number \n[Number_Warn]: 1 \n[Reason]: Некооректый список"
}



def add_fatal_error(Type_Error: int):
    Message = TYPE_FATAL_ERROR[Type_Error]
    Fatal_Error.append(Message)

def add_error(Type_Error: int):
    Message = TYPE_ERROR[Type_Error]
    Error.append(Message)

def add_warn(Type_Error: int):
    Message = TYPE_WARN[Type_Error]
    Warn.append(Message)   
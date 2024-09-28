from variable import Fatal_Error, Error, Warn, DEFAULT_ERROR_MESSAGE, DEFAULT_FATAL_ERROR_MESSAGE, DEFAULT_WARN_MESSAGE, bool_work

def check_fatal_error():
    for i in Fatal_Error:
        if i != "":
            eprint(DEFAULT_FATAL_ERROR_MESSAGE, i)
            
    bool_work = False      
        
def check_error():
    for i in Error:
        if i != "":
            eprint(DEFAULT_ERROR_MESSAGE, i)
            return

def check_warn():
    for i in Warn:
        if i != "":
            eprint(DEFAULT_WARN_MESSAGE, i)
            return



def eprint(Def_message="", pmessage=""):
    if Def_message == "" or pmessage == "":
        return
    
    print(Def_message + pmessage)
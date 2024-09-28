from variable import bool_work
import list, add_player

def _start():
    while bool_work:
        func = input("Введите число: ")
        match func:
            case "1":
                list_ = input("Введите список: ")
                print(list.sort_list(list_))
            case "2":
                add_player.start()
            case "9":
                exit()
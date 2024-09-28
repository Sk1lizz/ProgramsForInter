import add_error

def sort_list(list=""):
    if list == "":
        add_error.add_warn(1)
    else:
        split_list = list.split(" ")
        try:
            int_list = [int(item) for item in split_list]
            int_list_sort = sorted(int_list)
            list_sort = ""
            for i in int_list_sort:
                list_sort += f"{i} \n"
            return(list_sort)

        except:
            add_error.add_error(1)
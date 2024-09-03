def sort_list(list=" "):
    if list == " ":
        return
    else:
        split_list = list.split
        try:
            int_list = [int(i) for i in split_list]
        except:
            int_list = ""
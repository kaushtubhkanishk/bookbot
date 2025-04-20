def get_num_words(book_data):
    return len(book_data.split())

def get_symbols(book_data):
    symbols_dict = {}
    
    for i in range(len(book_data)):
        temp = book_data[i].lower()
        if temp in symbols_dict:
            symbols_dict[temp] += 1
        else:
            symbols_dict[temp] = 1
    
    return symbols_dict

def order_dict(symbols_dict):
    list_dict = []

    sorted_nums = sorted(symbols_dict.values())
    for i in reversed(sorted_nums):
        for x in symbols_dict.keys():
            if not x.isalpha():
                continue
            elif symbols_dict[x] == i:
                list_dict.append({f"{x}": f"{i}"})

    return list_dict

import collections
def getCardId(line: str) -> int :
    split_id_data = line.split(":")
    str_game_id = split_id_data[0].split(" ")[-1]
    return int(str_game_id) if str_game_id.isdigit() else 0


def getWinningNumber(line: str) -> list :
    split_id_data = line.split(":")
    str_list = split_id_data[1].strip().split("|")[0].strip().split(" ")
    while "" in str_list:
        str_list.remove("")
    return list(map(int, str_list))


def getPlayingNumber(line: str) -> list :
    split_id_data = line.split(":")
    str_list = split_id_data[1].strip().split("|")[1].strip().split(" ")
    while "" in str_list:
        str_list.remove("")
    return list(map(int, str_list))

def getListIntersection(list1: list, list2: list) -> list: 
    result = collections.Counter(list1) & collections.Counter(list2)
    return list(result)
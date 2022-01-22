def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    for x in data:
        if x.isdigit():
            list.append(x)
    return list

# Read data from file

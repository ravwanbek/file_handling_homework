def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    
    for x in data:
        if not x.isdigit():
            list.append(x)

    return list

# Read data from file

def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list=[]
    n=0
    for x in data:
        if x.isnumeric():
            n+=int(x)
            list.append(n)
    return n
# Read data from file

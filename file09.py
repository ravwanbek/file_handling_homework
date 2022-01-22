def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    min=0
    for x in data:
        if x.isnumeric():
            if int(x)<int(min):
                min=x

    
    return min
# Read data from file

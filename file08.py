def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
    max=0
    for x in data:
        if x.isnumeric():
            if int(x)>int(max):
                max=x

    
    return max

# Read data from file





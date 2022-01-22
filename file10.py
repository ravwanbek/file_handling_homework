def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list1=[]
    largest=0
    row=data.split('\n')
    for i in row:
        list1.append(len(i))
    print(list1)
    for j in list1:
        if j>largest:
            largest=j


    return largest
# Read data from file

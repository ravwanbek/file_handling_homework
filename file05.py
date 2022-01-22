from re import A


def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    a=0
    b=0
    
    for x in data:
        if x.isdigit():
            a+=1
        else: b+=1
    list.insert(0,a)
    list.insert(1,b)

    return list

# Read data from file

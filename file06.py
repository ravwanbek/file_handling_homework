def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    list1=[]
    row=data.split('\n')
    for i in row:
        list1.append(len(i))
    

    return list1
# Read data from file
f=open('txt_file\data06.txt').read()
print(main(f))
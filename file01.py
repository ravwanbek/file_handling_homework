def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list=[]
    for a in data.split(','):
        list.append(int(a))

    
    

    return list
    


    # Read data from file
    
    
f=open('txt_file\data01.txt')
txt=f.read()
print(main(txt))

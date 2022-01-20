def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    # Read data from file
    f=open('txt_file\data01.txt')
    txt=f.read()
    list=txt.split()
    return list
print(main(open('txt_file\data01.txt')))

def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=len(data)
    return a

# Read data from file
f=open('txt_file\data02.txt')
txt=f.read()
print(main(txt))
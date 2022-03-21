import json
import os


def save_v(en:str,vn:str):
    """Save data
    Args:
        en (str): english
        vn (str): viet name
    Returns:
        True: save new
        False: already exsits
    """
    old_data = {}
    if os.path.isfile("lib.json"):  
        with open("lib.json","r",encoding='utf8') as file_read:
            text =file_read.read()
            try:
                old_data = json.loads(text)
            except:
                old_data = {}
    if old_data.get(en):
        old_data[en]["count"]+=1
        with open("lib.json","w",encoding='utf8') as file:
            file.write(str(old_data).replace("'",'"'))
        return False
    
    old_data[en]={
        "count":1,
        "vn":vn
    }
    with open("lib.json","w",encoding='utf8') as file:
        file.write(str(old_data).replace("'",'"'))
    return True
        
        
def read_v(en:str)->(dict):
    """Save data

    Args:
        en (str): english
        vn (str): viet name

    Returns:
        dict: {"count":xx, "vn":yy}
        None: not exists
    """
    old_data = {}
    if os.path.isfile("lib.json"):  
        with open("lib.json","r",encoding='utf8') as file_read:
            try:
                old_data = json.loads(file_read.read())
            except:
                old_data = {}
    return old_data.get(en)


    
    
    
    
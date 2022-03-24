import json
import os
from firebase import firebase

url = "https://tuvung-f970c-default-rtdb.asia-southeast1.firebasedatabase.app/"
collection = "TuVung"
FIREBASE = firebase.FirebaseApplication(url, None)



def save_v(en:str,vn:str,count:int = None):
    """Save data
    Args:
        en (str): english
        vn (str): viet name
    Returns:
        True: save new
        False: already exsits
    """
    global FIREBASE,collection
    old_data = FIREBASE.get(collection,name="")
    if old_data:
        for key in old_data:
            data = old_data[key]
            if data.get("en") == en:
                FIREBASE.put(f"{collection}/{key}","count",data["count"]+1)
                return False
    data = {
        "en":en,
        "vn":vn,
        "count":1
    }
    if count:
        data["count"] = count
    FIREBASE.post(f"{collection}",data)
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
    global FIREBASE,collection
    old_data = FIREBASE.get(collection,name="")
    for key in old_data:
        data = old_data[key]
        if data.get("en") == en:
            return {"count":data.get("count"),"vn":data.get("vn")}
    return None


    
# old_data = {}
# if os.path.isfile("lib.json"):  
#     with open("lib.json","r",encoding='utf8') as file_read:
#         text =file_read.read()
#         try:
#             old_data = json.loads(text)
#         except:
#             old_data = {}

# for data in old_data:
#     save_v(en = data,vn = old_data[data].get("vn"),count = old_data[data].get("count"))
    

# def save_v(en:str,vn:str):
#     """Save data
#     Args:
#         en (str): english
#         vn (str): viet name
#     Returns:
#         True: save new
#         False: already exsits
#     """
#     old_data = {}
#     if os.path.isfile("lib.json"):  
#         with open("lib.json","r",encoding='utf8') as file_read:
#             text =file_read.read()
#             try:
#                 old_data = json.loads(text)
#             except:
#                 old_data = {}
#     if old_data.get(en):
#         old_data[en]["count"]+=1
#         with open("lib.json","w",encoding='utf8') as file:
#             file.write(str(old_data).replace("'",'"'))
#         return False
    
#     old_data[en]={
#         "count":1,
#         "vn":vn
#     }
#     with open("lib.json","w",encoding='utf8') as file:
#         file.write(str(old_data).replace("'",'"'))
#     return True
        
        
# def read_v(en:str)->(dict):
#     """Save data

#     Args:
#         en (str): english
#         vn (str): viet name

#     Returns:
#         dict: {"count":xx, "vn":yy}
#         None: not exists
#     """
#     old_data = {}
#     if os.path.isfile("lib.json"):  
#         with open("lib.json","r",encoding='utf8') as file_read:
#             try:
#                 old_data = json.loads(file_read.read())
#             except:
#                 old_data = {}
#     return old_data.get(en)


    
    
    
    
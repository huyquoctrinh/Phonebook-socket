import json 
import base64
import cv2
f = open("data.json","r")
data = json.load(f)
# print(data)

def load_data():
    f = open("data.json","r")
    data = json.load(f)

    return data

def convert_json_data(data):
    print(data)
    data_processed = json.loads(data)
    return data_processed

def gen_base64(imgdir):
    img = cv2.imread(imgdir)
    retval, buffer = cv2.imencode('.jpg', img)
    jpg_as_text = base64.b64encode(buffer)
    return jpg_as_text.decode('utf-8')

def find_someone(data,key, value):
    
    if key == "id":
        return data[value]
    else:
        res = dict()
        for i in range(len(data.values())):
            if list(data.values())[i][key]== value:
                data_final = dict()
                data_final["fullname"] = list(data.values())[i]["fullname"]
                data_final["phone"] = list(data.values())[i]["phone"]
                data_final["email"] = list(data.values())[i]["email"]
                data_final["dob"] = list(data.values())[i]["dob"]
                data_final["full"] = gen_base64(list(data.values())[i]["avatar"])
                res["U"+str(i)] = data_final
        return res
    
res =  find_someone(data,"email","trnhquchuy@yahoo.com.vn")
# print(res) 

data = dict()
data["img"] = gen_base64("./img/full/huy.jpeg")
msg = json.dumps(res)
# print(msg)
# with open('test.txt', 'wb') as f_output:
#     f_output.write()
# print()
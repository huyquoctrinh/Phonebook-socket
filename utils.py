import json 

f = open("data.json","r")
data = json.load(f)
# print(data)

def load_data():
    f = open("data.json","r")
    data = json.load(f)
    return data
# def get_data(json_data,cat = "",value = ""):
#     for json in json_data:
#         print(json)
#     #     if json[cat] == value:
#     #         return json
#     # return dict()
# print(get_data(data,"fullname","Trinh Quoc Huy"))

def convert_json_data(data):
    data_processed = json.loads(data.decode("utf8"))
    return data_processed
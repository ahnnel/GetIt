import requests
from flask import session
import eel
import json
import os
session = requests.session()
global ip

header = {"content-type": "application/json"}

# GETTING SELF IP
@eel.expose
def get_ip():
    ip = os.popen("ipconfig")
    output="Error getting ip"
    for line in ip.readlines():
        if "IPv4 Address" in line:
            start = line.find(":")
            end = -1
            output = line[start + 2:end]
            break
    return output

# CREATE CONNECTION
@eel.expose
def start_app(ip,port,host,user,password,db):
    try:
        data1 = {"ip": get_ip(),"host":host,"user":user,"password":password,"db":db}
        r = session.post("http://"+ip+":"+port+"/api/start_app",data=json.dumps(data1), headers=header)
        print("Connection OK")
        stat="Connection OK"
        return stat
    except:
        print("Connction Failed")
        stat = "Connection Failed"
        return stat

# DOWNLOAD IMAGE
@eel.expose
def download_image(url_path,file):
    myfile = requests.get(url_path+file)
    try:
        open('downloaded-images/'+file, 'wb').write(myfile.content)
        print("downloaded")
    except:
        print("download failed")

# FIND ENTRY
@eel.expose
def find_entry(ip,field0,char0,field1,char1,field2,char2,field3,char3,field4,char4,field5,char5,field6,char6,field7,char7):
    data1 = {"input_0":field0, "input_1": char0,"input_2":field1, "input_3": char1,"input_4":field2, "input_5": char2,"input_6":field3, "input_7": char3,"input_8":field4, "input_9": char4,"input_10":field5, "input_11": char5,"input_12":field6, "input_13": char6,"input_14":field7, "input_15": char7}
    r = session.post("http://"+ip+":1337/api/show_entry", data=json.dumps(data1), headers=header)
    data = r.json()
    print(data)
    return data

# ADD ENTRY
@eel.expose
def add_entry(ip,input_0,input_1,input_2,input_3,input_4,input_5,input_6,input_7,input_8):
    data1 = {"code":input_0, "department": input_1,"company":input_2, "name": input_3, "description": input_4,"color":input_5, "units": input_6,"price":input_7,"image":input_8}
    r = session.post("http://"+ip+":1337/api/add_entry", data=json.dumps(data1), headers=header)
    print ("add posted")
    data = r.json()
    print(data)
    return data

# UPLOAD IMAGE
@eel.expose
def upload_image(ip,input_1):
    try:
        files = {
            'file': (
                os.path.basename(input_1),
                open(input_1, 'rb'),
                'application/octet-stream'
            )
        }
        requests.post("http://" + ip + ":1337/api/upload_image", files=files)
        print("uploaded")
    except:
        print("failed")


# UPDATE ENTRY
@eel.expose
def update_entry(ip,input_0,input_1,input_2,input_3,input_4,input_5,input_6,input_7,input_8,input_9):
    print("UPD RECV")
    data1 = {"ID":input_0,"code":input_1, "department": input_2,"company":input_3, "name": input_4, "description": input_5,"color":input_6, "units": input_7,"price":input_8,"image":input_9}
    r = session.post("http://"+ip+":1337/api/update_entry", data=json.dumps(data1), headers=header)
    data = r.json()
    print(data)
    return data

# DELETE ENTRY
@eel.expose
def delete_entry(ip,input_0):
    print("DEL RECV")
    data1 = {"ID":input_0}
    r = session.post("http://"+ip+":1337/api/delete_entry", data=json.dumps(data1), headers=header)
    data = r.json()
    print(data)
    return data

# QUIT APP
@eel.expose
def quit_app():
    quit()

# STARTING APP
eel.init('')
eel.start('interface.html', size=(1300,1000), port=1337)

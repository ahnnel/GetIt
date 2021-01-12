from flask import Flask, request, jsonify, send_from_directory
import mysql.connector
from serverClasses import *
import os

global found_match, current_ip

app = Flask("GetIt API Server", static_url_path='')
app.secret_key = "ajsd8h218hd8hcs8hj9219ejd9ch8mc91u239m921cvu39du2191jd"
app.config["CLIENT_IMAGES"] = "Server-images/"


# CREATE CONNECTION
@app.route('/api/start_app', methods=["POST"])
def start_app():
    global host, user, password, db
    current_ip = str(request.json["ip"])
    host = str(request.json["host"])
    user = str(request.json["user"])
    password = str(request.json["password"])
    db = str(request.json["db"])

    print("CONNECTED> " + current_ip)
    return jsonify({"success": True})


# DOWNLOAD IMAGE
@app.route("/getimage/<path:image_name>", methods=['GET', 'POST'])
def getimage(image_name):
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=image_name, as_attachment=True)
    except FileNotFoundError:
        print(404)


# SHOWING ENTRIES
@app.route('/api/show_entry', methods=["POST"])
def show_entry():
    global mydb
    product = Product(0, str(request.json["input_1"]), str(request.json["input_3"]), str(request.json["input_5"]),
                      str(request.json["input_7"]), str(request.json["input_9"]), str(request.json["input_11"]),
                      str(request.json["input_13"]), str(request.json["input_15"]))
    field = Field("ID", str(request.json["input_0"]), str(request.json["input_2"]), str(request.json["input_4"]),
                  str(request.json["input_6"]), str(request.json["input_8"]), str(request.json["input_10"]),
                  str(request.json["input_12"]), str(request.json["input_14"]))
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
    except:
        print("Connection error")
    mycursor = mydb.cursor()
    sql = ('''
                    SELECT Json_object("ID",id,"Code",code,"Department",department,"Company",company,"Name",name,"Description",description,"Color",color,"Units",units,"Price",price,"Image",image) from db1.products WHERE ''' +
           field.code + ''' LIKE"''' + product.code + '''%" AND ''' + field.department + ''' LIKE"''' + product.department + '''%" AND ''' + field.company + ''' LIKE "''' + product.company + '''%" AND ''' + field.name + ''' LIKE "''' + product.name + '''%" AND ''' + field.description + ''' LIKE "''' + product.description + '''%" AND ''' + field.color + ''' LIKE "''' + product.color + '''%" AND ''' + field.units + ''' = "''' + product.units + '''"   AND ''' + field.price + ''' = "''' + product.price + '''";''');
    print(sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if myresult:
        x = myresult
        print(x)

    else:
        x = '''[['{"Match": "NO MATCHES"}']]'''

    z = jsonify(x)
    print(z)
    return z
    mydb.commit()


# UPLOAD IMAGE
@app.route('/api/upload_image', methods=["POST"])
def upload_image():
    image = request.files.get('file')
    image.save(('Server-images/' + image.filename))
    print("file saved - " + image.filename)
    return ("saved")


# ADD ENTRIES
@app.route('/api/add_entry', methods=["POST"])
def add_entry():
    newproduct = Product(0, str(request.json["code"]), str(request.json["department"]), str(request.json["company"]),
                         str(request.json["name"]), str(request.json["description"]), str(request.json["color"]),
                         str(request.json["units"]), str(request.json["price"]))
    file_image = str(request.json["image"])
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db1"
    )
    mycursor = mydb.cursor()
    try:
        sql = '''INSERT INTO db1.products (code,department,company,name,description,color,units,price,image) VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s); '''
        val = (newproduct.code, newproduct.department, newproduct.company, newproduct.name, newproduct.description,
               newproduct.color, newproduct.units, newproduct.price, file_image)
        mycursor.execute(sql, val)
        mydb.commit()
        x = '''[['{"response": "Added successfully"}']]'''
        return jsonify(x)

    except:
        x = '''[['{"response": "failed"}']]'''
        return jsonify(x)


# UPDATE ENTRIES
@app.route('/api/update_entry', methods=["POST"])
def update_entry():
    updproduct = Product(str(request.json["ID"]), str(request.json["code"]), str(request.json["department"]),
                         str(request.json["company"]), str(request.json["name"]), str(request.json["description"]),
                         str(request.json["color"]), str(request.json["units"]), str(request.json["price"]))
    file_image = str(request.json["image"])
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db1"
    )
    mycursor = mydb.cursor()
    print("IMAGE:>" + file_image)
    try:
        if file_image != "":
            sql = "UPDATE db1.products SET code=%s,department=%s,company=%s,name=%s ,description=%s,color=%s,units=%s,price=%s,image=%s WHERE ID=" + updproduct.ID + ";"
            val = (updproduct.code, updproduct.department, updproduct.company, updproduct.name, updproduct.description,
                   updproduct.color, updproduct.units, updproduct.price, file_image)
        else:
            sql = "UPDATE db1.products SET code=%s,department=%s,company=%s,name=%s ,description=%s,color=%s," \
                  "units=%s,price=%s WHERE ID=" + updproduct.ID + "; "
            val = (updproduct.code, updproduct.department, updproduct.company, updproduct.name, updproduct.description,
                   updproduct.color, updproduct.units, updproduct.price)
        print("UPDATE_>>>" + sql)
        mycursor.execute(sql, val)
        mydb.commit()
        x = '''[['{"response": "Updated successfully"}']]'''
        return jsonify(x)
    except:
        x = '''[['{"response": "failed"}']]'''
        return jsonify(x)


# DELETE ENTRIES
@app.route('/api/delete_entry', methods=["POST"])
def delete_entry():
    delproduct = Product(request.json["ID"], "", "", "", "", "", "", "", "")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db1"
    )
    mycursor = mydb.cursor()

    try:
        sql = "SELECT image FROM products WHERE ID=" + delproduct.ID + ";"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if myresult:
            x = myresult[0]
            y = ''.join(x)
            if y != "":
                os.remove("Server-images/" + y)
    except:
        x = '''[['{"response": "error"}']]'''
    try:

        sql = "DELETE FROM products WHERE ID=" + delproduct.ID + ";"
        print("DELETE_>>>" + sql)
        mycursor.execute(sql)
        mydb.commit()

        x = '''[['{"response": "Deleted successfully"}']]'''
        return jsonify(x)
    except:
        x = '''[['{"response": "failed"}']]'''
        return jsonify(x)


debug = True
app.run(host='0.0.0.0', port=1337, debug=debug)

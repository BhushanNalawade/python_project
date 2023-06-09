from flask import Flask,request,jsonify
import Product_Dao
from sql_connection import get_sql_connection
import json 
 
import orders_dao
import uim_dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getUIM', methods=['GET'])
def get_uim():
    response = uim_dao.get_uims(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getProducts', methods= ['GET'])

def get_Products():
    Products = Product_Dao.get_all_products(connection)
    response = jsonify(Products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    Product_id = Product_Dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'Product_id': Product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = Product_Dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("starting flask server")
    app.run(port=5000)
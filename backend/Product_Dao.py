# import mysql.connector

from sql_connection import get_sql_connection
def get_all_products(connection):
    
    cursor = connection.cursor()
    query = ("SELECT products.Product_id,products.name,products.uim_id,products.price_per_unit,uim.uim_name from products INNER JOIN uim on products.uim_id=uim.uim_id")

    cursor.execute(query)

    response = []
    for (Product_id,name,uim_id,price_per_unit,uim_name) in cursor:
        response.append(
            {
                'Product_id':Product_id,
                'name':name,
                'uim_id':uim_id,
                'price_per_unit':price_per_unit,
                'uim_name':uim_name
            }
        )

    
    return response


def insert_new_products(connection,product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (product_id,name,uim_id,price_per_unit) VALUES(%s,%s,%s,%s)")

    data = (product['product_id'],product['product_name'],product['uim_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid


def delete_products(connection,product_id):
    
    cursor = connection.cursor()
    query = ("Delete from products where product_id=" +str(product_id))

    
    cursor.execute(query)
    connection.commit()


if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_products(connection,0))
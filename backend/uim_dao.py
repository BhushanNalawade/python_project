
def get_uims(connection):
    cursor = connection.cursor()
    query = ("select * from uim")
    cursor.execute(query)
    response = []
    for (uim_id, uim_name) in cursor:
        response.append({
            'uim_id': uim_id,
            'uim_name': uim_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uims(connection))
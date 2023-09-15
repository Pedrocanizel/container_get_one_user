import psycopg2
import pandas as pd
import json


def get_connect():
    con = psycopg2.connect(host='', database='',
    user='', password='')
    return con



def select(name, email):
    conn = get_connect()
    cursor = conn.cursor()
    query = f"""SELECT * FROM schema.table WHERE search_id = '{name}-{email}';"""
    df = pd.read_sql_query(query, con=conn)
    rows = df.to_json(orient='records')
    rows = json.loads(rows)
    return rows

    

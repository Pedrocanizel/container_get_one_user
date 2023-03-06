import psycopg2
import datetime
import pandas as pd
import json


def get_connect():
    con = psycopg2.connect(host='localhost', database='bit_pro',
    user='postgres', password='123')
    return con



def select(email):
    conn = get_connect()
    cursor = conn.cursor()
    query = f"""SELECT * FROM public.cadastro_usuario WHERE email LIKE '%{email}%';"""
    df = pd.read_sql_query(query, con=conn)
    rows = df.to_json(orient='records')
    rows = json.loads(rows)
    return rows

    
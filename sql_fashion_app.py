import sqlite3
import gemini_utility as genai
import streamlit as st

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    print(sql+" "+db)
    cur.execute(sql)
    conn.commit()
    rows=cur.fetchall()
    conn.close()
    return rows

prompt=[
    """
    You are an expert in converting English questions to sql query!
    the fashion database has the name fashion table and has columns - USER_ID ,PRODUCT_ID ,PRODUCT_NAME ,BRAND ,CATEGORY,PRICE,COLOR,SIZE 
    for example :how many entries of records are present ?
    the sql command will be something like this SELECT COUNT (*) FROM fashion;
    example 2:Tell me all the data of user_id is 1?
    the sql command will be something like this SELECT * FROM fashion where user_id =1;
    also the sql code should not have ``` in beginning or end and sql word output in a single line
    """
]

st.title("Fashion DB")
input=st.text_input("enter a query")
submit=st.button("ask a query")
if submit:
    resp=genai.get_gemini_pro_response([prompt[0],input])
    st.write(resp)
    rows=read_sql_query(resp, "fashion.db")
    for row in rows:
        st.write(row)
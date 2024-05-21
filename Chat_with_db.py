import sqlite3
import gemini_utility as genai
import streamlit as st

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.close()
    return rows

prompt=[
    """
    You are an expert in converting English questions to sql query!
    the sql database has the name Student and has columns
    for example :how many entries of records are present ?
    the sql command will be something like this SELECT COUNT (*) FROM Student;
    example 2:Tell me all the students studying in data science class?
    the sql command will be something like this SELECT * FROM Student where CLASS =" DATA SCIENCE";
    also the sql code should not have ``` in beginning or end and sql word output
    """
]

st.title("Chat with db")
input=st.text_input("enter a query")
submit=st.button("ask a query")
if submit:
    resp=genai.get_gemini_pro_response([prompt[0],input])
    st.write(resp)
    rows=read_sql_query(resp, "Student.db")
    for row in rows:
        st.write(row)
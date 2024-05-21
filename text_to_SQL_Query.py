import gemini_utility as genai
import streamlit as st

st.title("TEXT TO SQL QUERY GENERATOR")
input_text= st.text_area("Enter your query in plain english")
submit=st.button("Generate SQL Query")
if submit:
    with st.spinner("Running ... Please Wait"):
        template="""
        Create SQL Query using the below text
        ```
        {sql_input}
        ```
        I just want a sql query
        """
        formatted_template=template.format(sql_input=input_text)
        resp=genai.get_gemini_pro_response(formatted_template)
        st.subheader("Response is")
        st.write(resp)
        #Generating Expected Output
        expected_output="""
        What would be the expected response of this SQL Statement :
        ```
        {sql_query}
        ```
        provide the sample tabular response with no explanation.
        """
        expected_output_format=expected_output.format(sql_query=resp)
        response=genai.get_gemini_pro_response(expected_output_format)
        st.write(response)
        #GENERATION  Explaination
        explaination="""
            Explain this sql query {sql_query}, please provide simplest of explaination
        """
        explaination_format=explaination.format(sql_query=resp)
        explaination_resp=genai.get_gemini_pro_response(explaination_format)
        st.subheader("Explaination is")
        st.write(explaination_resp)
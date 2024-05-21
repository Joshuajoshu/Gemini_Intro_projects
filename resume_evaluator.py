import gemini_utility as genAi
import streamlit as st
import PyPDF2 as pdf

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text=""
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text+= str(page.extract_text())
    return text

input_prompt = """
    Hey Act Like a skilled or very experience ATS(Application Tracking System) with a deep understanding of tech field,
    software engineering, data science, data analyst and big data engineer. Your task is to evalutate the resume based 
    on the job description.
    You must consider the job market is very competitive and you should provide best assistance for improving their
    resumes. Assign the percentage Matching based on Jd and the missing keywords with high accuracy
    description: {jd}
    Resume-text : {text}
    I want the response in one single string having the structure
    {{"JD Match": "%", "MissingKywords: []", "Profile Sumary":""}}
"""

st.title("Resume Evaluator")
jd = st.text_area("Provide Your Job Description")
input_prompt_format = input_prompt.format(jd=jd, text="")
uploaded_file = st.file_uploader("Upload your resume",type="pdf")
submit = st.button("Evaluate")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        input_prompt_format = input_prompt.format(jd=jd,text=text)
        resp = genAi.get_gemini_pro_response(input_prompt_format)
        st.write(resp)

print("Done.")
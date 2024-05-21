from flask import Flask ,render_template, redirect, url_for
import streamlit as st
import subprocess
import time

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h2 style="text-align: center;"> The Projects that we have done on GEMINI LLM </h2>
    <form style="text-align: center;" action='/calorie_advisor' method='get'>
        <button type='submit'>Calorie_Advisor</button>
    </form>
    <form style="text-align: center;" action='/text_to_text_LLM' method='get'>
        <button type='submit'>Text_to_Text LLM</button>
    </form>
    <form style="text-align: center;" action='/image_to_text_LLM' method='get'>
        <button type='submit'>Image_to_Text LLM</button>
    </form>
    <form style="text-align: center;" action='/healthy_advisor_LLM' method='get'>
        <button type='submit'>Healthy Advisor LLM</button>
    </form>
    <form style="text-align: center;" action='/Medical_Image_Research_LLM' method='get'>
        <button type='submit'>Medical Image Research LLM</button>
    </form>
    <form style="text-align: center;" action='/resume_evaluator' method='get'>
        <button type='submit'>Resume Evaluator LLM</button>
    </form>
    <form style="text-align: center;" action='/talk_with_an_img_app' method='get'>
        <button type='submit'>Talking with an Image</button>
    </form>
    <form style="text-align: center;" action='/youtube_transcript' method='get'>
        <button type='submit'>Youtube Transcriptor</button>
    </form>
    <form style="text-align: center;" action='/chatbot' method='get'>
        <button type='submit'>A Generative AI ChatBot</button>
    </form>
    <form style="text-align: center;" action='/bill_qna' method='get'>
        <button type='submit'>A ChatBot for a given Bill</button>
    </form>
    <body>
    """
@app.route('/text_to_text_LLM')
def run_text_to_text():
    subprocess.Popen(["streamlit", "run", "ui-texttotext.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/image_to_text_LLM')
def run_image_to_text():
    subprocess.Popen(["streamlit", "run", "ui-imagetotext.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/healthy_advisor_LLM')
def run_health_advisor():
    subprocess.Popen(["streamlit", "run", "healthy_advisor.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/calorie_advisor')
def run_calorie_advisor():
    subprocess.Popen(["streamlit", "run", "calorie_advisor.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/Medical_Image_Research_LLM')
def run_medical_img():
    subprocess.Popen(["streamlit", "run", "medical_img.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/resume_evaluator')
def run_resume_evaluator():
    subprocess.Popen(["streamlit", "run", "resume_evaluator.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/talk_with_an_img_app')
def run_talk_with_img():
    subprocess.Popen(["streamlit", "run", "talk_with_an_image.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/youtube_transcript')
def run_youtube_transcrip():
    subprocess.Popen(["streamlit", "run", "Youtube.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/chatbot')
def run_chatbot():
    subprocess.Popen(["streamlit", "run", "chatbot.py"])
    time.sleep(5)
    return redirect(url_for('index'))

@app.route('/bill_qna')
def run_bill_qna():
    subprocess.Popen(["streamlit", "run", "bill_qna.py"])
    time.sleep(5)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

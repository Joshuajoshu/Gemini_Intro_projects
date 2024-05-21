import gemini_utility as genai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

# print("Done")
def extract_transcipt_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        transcript=""
        for i in transcript_text:
            transcript+=" "+i["text"]
        return transcript
    except Exception as e:
        raise e

# k=input()
# extract_transcipt_details(k)
prompt= """
    You are youtube video summarizer. you wll be taking the transcript text and summarizing
    the entire video and providing the
    important points within 250 words. Please provide the summary of the given text given here 
"""

st.title ("Youtube Transcript Generator")
youtube_link=st.text_input("Enter Youtube Video Link ")
if youtube_link:
    video_id=youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)

button=st.button("Generate Summary")
if button:
    transcript_text=extract_transcipt_details(youtube_link)
    if transcript_text != "":
        resp=genai.get_gemini_pro_response(prompt+transcript_text)
        st.write(resp)
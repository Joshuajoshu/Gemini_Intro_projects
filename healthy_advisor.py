import gemini_utility as genai
import streamlit as st

from PIL import Image

st.title("Health Advisor - Gemini App")
uploaded_file=st.file_uploader("upload a dish or food",type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Food pic",use_column_width=True)



prompt="""
You are an expert in nutritioninst and doctor where you need to see the food items and dishes 
from the image and give a very few words of rating of healthyness of taking the particular dish
"""
input=st.text_input("Enter the disease you have ")
submit =st.button("Healthy tips")
if submit:
    resp=genai.get_gemini_pro_vision_response(prompt,image)
    st.subheader("Response is")
    st.write(resp)
    template="""
    the list of reactions that a person can having a disease of
    ```
    {disease}
    ```
    eat the dish that is in the image
    and give suggestions as example ofIf you have a fever, you should avoid eating paella because it is a hot dish and could make your fever worse. You should also avoid eating other hot foods, such as soups and stews. Instead, you should eat cool foods, such as fruits and vegetables. You should also drink plenty of fluids to stay hydrated.

    If your fever is severe or does not improve after a few days, you should see a doctor.
    """
    avoid_format=template.format(disease=input)
    avoid_diseases=genai.get_gemini_pro_vision_response(avoid_format,image)
    st.subheader("the diseases and side effects of the dish")
    st.write(avoid_diseases)
    preferred_template="""
    give a choice of options ( early morning snack, breakfast,lunch, evening snack, dinner) of when the dish would be
    preferred to eat and give a 2 lines explaination of why
    """
    preferred_meal=genai.get_gemini_pro_vision_response(preferred_template,image)
    st.subheader("Preferred")
    st.write(preferred_meal)
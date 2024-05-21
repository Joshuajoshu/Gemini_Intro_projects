import streamlit as st
import gemini_utility as genai

from PIL import Image

st.title("Medical Inage Analysis LLM APP")
upload = st.file_uploader("Choose a file ",type=['jpg','png','jpeg'])
image=""
if upload is not None:
    image=Image.open(upload)
    st.image(image,caption="Medical Image",use_column_width=True)
# input=st.text_input("Enter your prompt")
submit=st.button("Generate Analysis")

input_prompt="""
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present the images.
You Responsibilities include:
1. Detailed Analysis: Thoroughly identify each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.
Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues. 
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
3. Disclaimer: Accompany your analysis with disclaimer: "Consult with a Doctor before making any decisions."
4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above.

Please provide me an output response with these 4 headings detailed analysis,finding report, recommendation and next steps ,treatment suggestions

"""
if submit:
    resp=genai.get_gemini_pro_vision_response(input_prompt,image)
    st.write(resp)
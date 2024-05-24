
### app.py
Save your provided code as `app.py` in the repository:

```python
### Medical Diagnostic App
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Initialize our Streamlit app

st.set_page_config(page_title="Medical Diagnostic App")

st.header("Medical Diagnostic App")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Diagnose the Image")

input_prompt = """
Analyze the uploaded medical image, which may include X-rays, MRIs, CT scans, or ultrasound images. First, identify the type of medical imaging used and the specific body part or organ depicted. Carefully examine the image for any abnormalities, such as fractures, tumors, lesions, or signs of disease.

Based on the visual information, provide a detailed diagnostic interpretation. Highlight key features in the image that support your diagnosis, such as size, location, and appearance of any anomalies. Compare these features with standard medical criteria for diagnosing conditions relevant to the image.

Once a diagnosis is made, offer a concise summary of the findings in layman's terms. This should include a brief explanation of the identified condition, potential causes, and implications for the patient's health.

End with recommendations for next steps. This might include suggesting further medical tests for confirmation, recommending a consultation with a specialist, or advising immediate medical attention, depending on the severity of the findings.

Emphasize that this AI-generated diagnosis is preliminary and should be followed up with a consultation with a healthcare professional for a conclusive diagnosis and personalized medical advice
"""

## If submit button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)

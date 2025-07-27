###health Management App
from dotenv import load_dotenv
load_dotenv()##load all the enivromnet variable
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('OPENAI_API_KEY'))

###main function-- func to load google gemini vision api
def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response= model.generate_content([input,image[0],prompt])
    return response.text




###function input img setup
def input_image_setup(uploaded_file):
    #check if a file has been uploaded
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()


        image_parts = [
            {
                "mime_type": uploaded_file.type,
              
                "data": bytes_data
            }
        ]
        return image_parts
    
    else:
        raise FileNotFoundError("No file uploaded")
    

 ##intialise our streamlit app
input_prompt = """
You are an expert in nutritionist AI model. where you need to see the food items , identify each food item, and calculate the total catlerios and provide the detail in the below format 
         1.item1 - no of calories
         2.item2 - no of calories
"""       

st.set_page_config(page_title = "AI nutritionist App")

st.header("AI nutritionist App")
input = st.text_input("input prompt: ",key="input")
uploaded_file = st.file_uploader("choose an image ...", type=["jpg","png","jpeg"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded image",use_column_width=True)

submit_button = st.button("tell me the totla calories")

#if submit button is click
prompt=""
if submit_button:
   image_data = input_image_setup(uploaded_file)
   response = get_gemini_response(input_prompt,image_data,prompt)
   st.subheader("the Response is ")
   st.write(response)
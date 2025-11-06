from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content,prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    reponse =model.generate_content([input,pdf_content[0],prompt])
    return reponse.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images =pdf2image.convert_from_bytes(uploaded_file.read())
        first_page= images[0]
        
        #convert into bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##Streamlit app 
st.set_page_config(page_title="ATS Resume Expert")
st.header("Application tracking System")
input_text =st.text_area("Job Description", key= "input")
uploaded_file =st.file_uploader("Upload your resume(PDF)...",type=["pdf"])

if uploaded_file is None:
    st.write("File Uploaded Sucessfully")

sumbit1 = st.button("Tell me about the resume")
sumbit2 = st.button("How can i improve my resume")
sumbit3 = st.button("Percentage match")

input_prompt1 = """
Analyze the candidate’s resume against the provided job description. Give a brief professional summary highlighting their background, education, and
key strengths. Then describe their main strengths where they meet or exceed the JD, followed by gaps or missing skills where they fall short. Suggest a 
few clear, actionable improvements to increase their suitability for the role. Conclude with a short verdict on whether they should be shortlisted and 
why. Keep the answer concise and in paragraph form."""

input_prompt2 = """
Analyze this resume and give a concise single-paragraph review. Start with a brief summary of the candidate’s background and level. Highlight what works 
well (format, structure, tone, clarity, keywords). Then note key weaknesses (missing keywords, vague phrasing, lack of metrics, inconsistent formatting). 
Provide specific, actionable fixes (rewrite bullets with numbers, reorder sections, strengthen summary, align wording to target roles/industry). 
Close with recommended skills/certifications/experiences to add. Keep it direct, specific, and under ~150 words."""

input_prompt3 ="""
Analyze the resume against the JD and give a concise paragraph. Include: a percentage match (0–100%) based on required skills/tools, education, 
experience, and achievements; a brief rationale explaining what’s well covered vs. missing or weak; and 2–3 specific actions to raise the score 
(e.g., add key skills, refine keywords, gain/highlight relevant experience). Keep it tight, concrete, and use JD terminology."""

if sumbit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("Please upload the file ")

if sumbit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("Please upload the file ")

if sumbit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("Please upload the file ")
ATS Resume Analyzer – CS50 Final Project
Overview

ATS Resume Analyzer is an AI-powered application designed to evaluate and improve resumes by comparing them with job descriptions. The project simulates the behavior of modern Applicant Tracking Systems (ATS) used by companies to screen candidates during recruitment.

The system allows a user to upload their resume (in PDF format) and paste a job description (JD) into the text box. The app then uses Google’s Gemini Generative AI model to analyze both the resume and the job description, generating intelligent feedback such as a resume summary, improvement suggestions, and a percentage match score.

The purpose of this project is to make resume evaluation transparent and educational. Instead of guessing what recruiters or AI systems are looking for, users can see how well their resumes align with specific job postings — and what changes can increase their chances of being shortlisted.

Motivation

In today’s competitive job market, recruiters often rely on ATS software to filter hundreds of resumes based on keyword matches and role alignment. Many skilled applicants are rejected simply because their resumes lack the right phrasing or formatting for ATS scanning.

As someone interested in both AI and aeronautical engineering, I wanted to create a practical, real-world tool that uses artificial intelligence for meaningful career improvement. This project combines my interest in AI-based text analysis with a problem faced by nearly every job seeker — making it both technically challenging and personally relevant.

Features

Resume Upload – Users can upload their resumes in PDF format.

Job Description Input – Users paste the JD text into a provided box.

Three Analysis Options:

“Tell Me About the Resume” – Provides a short professional summary of the candidate, highlighting key strengths and weaknesses relative to the JD.

“How Can I Improve My Resume” – Generates detailed, point-wise feedback on formatting, structure, keyword optimization, tone, and missing skills.

“Percentage Match” – Calculates an approximate match score (0–100%) based on skills, experience, and alignment with the JD, along with actionable recommendations to raise the score.

User-Friendly Interface – Built using Streamlit, allowing users to interact easily without any coding knowledge.

AI-Driven Insights – Uses Google’s Gemini 2.5 Flash model to perform natural language comparison and reasoning.

Project Structure

Here’s an explanation of each file used in the project:

app.py – The main application file. It contains the Streamlit-based frontend, Google Gemini API integration, and logic to process resumes and job descriptions.

Handles file uploads using Streamlit’s file_uploader() function.

Defines three buttons, each mapped to a specific AI prompt for different types of analysis.

Calls the Gemini API and displays the response safely on the screen.

Includes error handling for missing files or invalid inputs.

.env – Stores the Google API key securely. The key is loaded into the environment using dotenv to prevent hardcoding sensitive information.

requirements.txt – Lists all required dependencies for the project (e.g., streamlit, google-generativeai, pdf2image, Pillow, python-dotenv). Installing from this file ensures easy setup on any system.

README.md – This documentation file, explaining the purpose, structure, and usage of the project.


Design Choices and Rationale

1. Using Streamlit for the Interface:
Streamlit offers a clean, Python-based framework to build interactive web apps quickly without front-end coding. It was ideal for this project because it allowed me to focus on logic, not layout.

2. Choosing Google Gemini (instead of OpenAI):
Gemini models provide strong multi-modal capabilities — meaning they can analyze both text and image-based PDFs. Since resumes are often uploaded as PDFs, Gemini’s visual understanding helps extract text more reliably than traditional parsing methods.

3. Handling Only the First Page of the Resume:
For simplicity, the system converts only the first page of the uploaded PDF into an image for analysis. Most resumes fit on one page, and this also reduces API costs and speeds up processing.

4. Separate Buttons for Each Analysis:
Instead of combining all outputs into one long response, I added three distinct buttons — giving users control over what they want to know. This makes the interface cleaner and more user-friendly.

5. Safety Checks and Error Handling:
The function get_gemini_response() includes safe checks to ensure that the model returns a valid response before displaying it, avoiding runtime errors and improving reliability.

Challenges Faced

Handling empty or corrupted PDFs initially caused runtime issues. This was resolved by converting the first page into an image using pdf2image.

Gemini occasionally returned empty responses (finish_reason=1). I solved this by adding a validation layer before accessing response.text.

Managing multiple button clicks in Streamlit required restructuring the code using elif to prevent reruns and variable resets.

How to Run the Project

Clone the repository and open it in your IDE.

Install the required packages:

pip install -r requirements.txt


Create a .env file and add your Gemini API key:

GOOGLE_API_KEY=your_api_key_here

Run the app:

streamlit run app.py

Open the local URL shown in your terminal to access the app.

Conclusion
The ATS Resume Analyzer demonstrates how AI can help bridge the gap between job seekers and modern recruitment systems. By combining text processing, AI reasoning, and an intuitive interface, it provides meaningful feedback that users can act upon immediately.
This project was a valuable learning experience in API integration, error handling, and front-end interactivity using Streamlit. It represents both technical growth and practical problem-solving — and I’m proud to submit it as my final project for CS50.

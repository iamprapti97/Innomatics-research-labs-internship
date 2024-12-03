import streamlit as st
import google.generativeai as genai

# Configure the API key and model
genai.configure(api_key="AIzaSyCsC_YDsc56I6V7jmeJbC5nkc14A4Ql2ow")
model = genai.GenerativeModel("models/gemini-1.5-flash")
chatbot = model.start_chat(history=[])

# Streamlit app header
st.set_page_config(page_title="An AI Code Reviewer", page_icon="📝")
st.title("An AI Code Reviewer")
st.markdown("Please submit your Python code, and I will review it for any potential bugs and suggest fixes.")

# Code input area
code_input = st.text_area("Paste your Python code here:", height=300, placeholder="Enter your Python code...")

# Function to process code review using the chatbot
def get_code_feedback(code):
    prompt = f"Please review the following Python code for bugs, errors, or areas for improvement. Provide suggestions and corrected code:\n\n{code}"

    try:
        # Sending the code for review to the AI model
        response = chatbot.send_message(prompt)
        return response.text.strip()  # Get and return the response
    except Exception as e:
        return f"An error occurred while reviewing the code: {str(e)}"

# Trigger review on button click
if st.button("Submit Code for Review"):
    if code_input:
        # Get feedback from AI
        review_feedback = get_code_feedback(code_input)

        # Display AI review and suggestions
        st.subheader("AI Code Review Results:")
        st.write(review_feedback)
        
        # Option to download the fixed code
        st.download_button(
            label="Download Reviewed Code",
            data=review_feedback,
            file_name="reviewed_code.py",
            mime="text/x-python-script"
        )
    else:
        st.warning("Please enter Python code to be reviewed.")


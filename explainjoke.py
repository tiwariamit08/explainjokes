import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


def get_joke_explanation(joke):

    response = client.chat.completions.create(
    model="gpt-4o",
        messages=[
            {"role": "user", "content": f"Explain the following joke: {joke}"}
        ]
)
    
    return response.choices[0].message.content

# Streamlit application
st.title("Joke Explainer")

# User input for joke
joke_input = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke_input:
        explanation = get_joke_explanation(joke_input)
        st.subheader("Explanation")
        st.write(explanation)
    else:
        st.error("Please enter a joke before submitting.")
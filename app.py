pip install langchain
pip install langchain_community
pip install fastapi
pip install uvicorn
pip install langchain-google-gena

import os
import warnings
from fastapi import FastAPI
from pydantic import BaseModel
from langchain import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

# Set up environment and API key
os.environ['GOOGLE_API_KEY'] = 'Use Your Key'
genai.configure(api_key='GOOGLE_API_KEY')
warnings.filterwarnings("ignore")

# Initialize FastAPI
app = FastAPI()

# Create the prompt template
prompt_template: str = """
You are a chatbot designed for negotiating product prices. Respond to the following question: {question}. Use a friendly and professional tone, offering clear options like accepting the price, rejecting it, or proposing a counteroffer. Avoid technical jargon and focus on making the negotiation simple and easy to understand.
"""

prompt = PromptTemplate.from_template(template=prompt_template)

# Instantiate the Google Generative AI instance
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.2, convert_system_message_to_human=True)


# Define the input model
class Question(BaseModel):
    question: str


@app.post("/negotiate")
async def negotiate_price(input: Question):
    # Format the prompt to add variable values
    prompt_formatted_str: str = prompt.format(question=input.question)

    # Make a prediction
    prediction = llm.predict(prompt_formatted_str)

    # Return the question and the prediction
    return {
        "question": input.question,
        "response": prediction
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)


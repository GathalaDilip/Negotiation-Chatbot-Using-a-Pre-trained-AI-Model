# Negotiation-Chatbot-Using-a-Pre-trained-AI-Model
Documentation for Integrating Google Generative AI (Gemini Pro) Model with FastAPI
This documentation explains the integration of the Google Generative AI (Gemini Pro) model using LangChain and FastAPI to create a chatbot for product price negotiation. The chatbot responds in a professional and friendly tone, offering options like accepting, rejecting, or counter-offering during negotiation.



# Google Generative AI Price Negotiation Chatbot

## Overview
This project integrates **Google's Generative AI (Gemini Pro)** using **LangChain** and **FastAPI** to build a chatbot that can negotiate product prices in a friendly and professional manner. The chatbot provides options like accepting the price, rejecting it, or making a counteroffer.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [API Example](#api-example)
- [Project Structure](#project-structure)
- [License](#license)

## Installation
To get started with this project, you need to install the required dependencies.

Run the following commands in your terminal:

```bash
pip install langchain
pip install langchain_community
pip install fastapi
pip install uvicorn
pip install langchain-google-genai




Setup
Set Google API Key:
This project requires a valid Google API key. Replace 'YOUR_GOOGLE_API_KEY_HERE' in the code with your actual Google API key.

Environment Setup:
In the code, set up the API key in the environment variables:



os.environ['GOOGLE_API_KEY'] = 'YOUR_GOOGLE_API_KEY_HERE'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])




Usage
After installing the required dependencies and setting up the API key, you can run the application.

Running the FastAPI Server:
Start the FastAPI server by executing the following command in the terminal:



uvicorn app:app --reload
This will start the server locally at http://localhost:8000.


API Example
Endpoint: /negotiate
This API endpoint accepts a POST request containing a negotiation question and returns an AI-generated response.

Example Request (POST):

{
    "question": "Can I get a discount on this product?"
}

Example Response:

{
    "question": "Can I get a discount on this product?",
    "response": "I understand you’re looking for a discount. We can offer a 5% discount on the current price, or you can bundle this product with another to get 10% off. Does this work for you?"
}



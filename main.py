import streamlit as st
from general_functions import get_env
#import torch
import accelerate
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


# Initialize the accelerator (not necessary if you are running this locally, with no GPU o TPU available))
accelerator = accelerate.Accelerator()

#let the user choose the model to load
model_dict = {'t5-small': 't5-small (translation)', 'databricks/dolly-v2-3b': 'dolly-v2-3b (general)'}

#ask the user to choose a model
model_name = st.selectbox('Choose a model', list(model_dict.keys()))

#display the model description
st.write('You have chosen a', model_dict[model_name])

# Load the model and tokenizer (not necessary if you are running this locally, with no GPU o TPU available)
instruct_pipeline = pipeline(model=model_name, trust_remote_code=True)

#inform the user that the model has been loaded
st.write('Model loaded')


#ask the user to input a question
question = st.text_input("Ask a question", "What is the meaning of life?")

#generate an answer using the pipeline
answer = instruct_pipeline(question)

#display the answer
st.write(answer)


#notes: for windows systems, models are downloaded in C:\Users\your-username\.cache\huggingface\transformers
#to cleare the cache, navigate to the folder mentioned above and delete folders and files.
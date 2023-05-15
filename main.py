import streamlit as st
from general_functions import get_env
#import torch
import accelerate
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


# Initialize the accelerator (not necessary if you are running this locally, with no GPU o TPU available))
accelerator = accelerate.Accelerator()

#let the user choose the model to load
#first create a dictionary of available models: include a simple model from huggingface and a more complex model from databricks
model_dict = {'t5-small': 't5-small', 'databricks/dolly-v2-3b': 'databricks/dolly-v2-3b'}

#ask the user to choose a model
model_name = st.selectbox('Choose a model', list(model_dict.keys()))


# Load the model and tokenizer (not necessary if you are running this locally, with no GPU o TPU available)
model_name = "databricks/dolly-v2-3b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
instruct_pipeline = pipeline(model="databricks/dolly-v2-3b", trust_remote_code=True)

#inform the user that the model has been loaded
st.write('Model loaded')

#ask the user to input a question
question = st.text_input("Ask a question", "What is the meaning of life?")

#generate an answer using the pipeline
#answer = instruct_pipeline(question, max_length=100, min_length=5, do_sample=True, temperature=0.7, top_k=50, top_p=0.95, num_return_sequences=3)
answer = instruct_pipeline(question)

#display the answer
st.write(answer)

#import Libraries
import streamlit as st 
import replicate 
import os 

#App title 
st.set_page_config(page_title="Llma Chatbot") 

#Replicate Credentials 
with st.sidebar:
    st.title('Llma Chatbot')
    #if "RELICATE_API_TOKEN" in st.secrets:
    #    st.success('API key already provideed!', icon="✅")
from langchain_ollama import OllamaLLM
import streamlit as st

st.title("Prompt Ultra")
sysprompt= ''' 
 want you to Act as an ai prompt engineer.

when I give you a task, I want you to respond with a enhanced prompt that is optimized for LLMs
the prompt(task) i want you to optimize for llms is: 
'''
model = OllamaLLM(model="llama3.2:1b")
catoptions = ["coding","creative writing","Classifcation"] 
st.radio("What Catagory",catoptions)
st.subheader("Describe Task")
Describtion = st.text_input("please describe the task for the LLM to do")

if st.button('Submit'):
    fullpromt = sysprompt +"  "+  Describtion
    airesponse = model.invoke(input=fullpromt)
    st.subheader("Your Ultra-powerful prompt is ")
    st.write(airesponse)



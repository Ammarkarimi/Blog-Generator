#! C:\Data\Python\venv\Scripts\python.exe

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import torch  # Ensure torch is imported

# Function to get response
def getLlamaResponse(input_text, blog_style, audience_level, tone, content_focus, structure):
    # Check if GPU is available and set device accordingly
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Calling Llama model and ensuring it runs on GPU if available
    llm = CTransformers(model='.\\model\\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        device= device,
                        config={
                            'temperature': 0.7,
                        }                        
                        )

    # Prompt Template
    template = """
   You are a blogger and you have to write a blog on {input_text}. You have to also keep in mind that you writing for {blog_style}. However the audience which you have are {audience_level}. Always write in {tone} manner. The main focmust be {content_focus} and Strictly follow the {structure}. Strictly give the correct and complete answer.
    """

    prompt = PromptTemplate(input_variables=['blog_style', 'input_text','audience_level','tone','content_focus','structure'],
                            template=template)

    # Generate response
    response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, audience_level=audience_level, tone=tone, content_focus=content_focus, structure=structure))
    return response

st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate the blog🤖")

input_text = st.text_input("Enter Blog Topic")

# Creating two more columns for additional fields

col1, col2 = st.columns([5, 5])

with col1:
    content_focus = st.selectbox("Content Focus", ('Overview', 'In-depth Analysis', 'Practical Tips', 'Case Study'), index=0)

with col2:
    blog_style = st.selectbox("Writing the blog for", ('Researcher', 'Data Scientist', 'Common People'), index=0)

# Additional Input Fields in Streamlit
col3, col4 = st.columns([5, 5])

with col3:
    audience_level = st.selectbox("Audience Level", ('Beginner', 'Intermediate', 'Advanced'), index=0)

with col4:
    tone = st.selectbox("Tone of Writing", ('Formal', 'Informal', 'Conversational', 'Technical'), index=0)

structure = st.selectbox("Preferred Structure", ('Listicle', 'Step-by-Step Guide', 'Narrative', 'Comparison'), index=0)

submit = st.button("Generate")

if submit:
    answer = getLlamaResponse(input_text, blog_style, audience_level, tone, content_focus, structure)
    st.write(answer)

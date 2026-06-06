from langchain_core.prompts import PromptTemplate

section_prompt = PromptTemplate(
    
    template ="""
    you are the professional research writer
    
    Write a detailed resaerch section on:
    
    section: {section}
    topic: {topic}
    
    Make the response
    -detailed
    -well structured
    -professional
    -easy to understand
    -properly formatted
    
    """,
    input_variables = ['section', 'topic']
)
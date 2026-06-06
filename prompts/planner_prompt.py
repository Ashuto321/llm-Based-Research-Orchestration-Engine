from langchain_core.prompts import PromptTemplate

planner_prompt = PromptTemplate(
    template ="""
     you are the expert Research Planner
     
     your task is to create 3 sections for a detailed report section on the given topic.
     
     topic: {topic}
     
     Return only the section headings in comma seperated values
     
     Example:
     introduction, application, challenges
    """,
    input_variables =['topic']
)
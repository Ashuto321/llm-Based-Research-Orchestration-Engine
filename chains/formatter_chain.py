from utils.fromatter import format_report
from langchain_core.runnables import RunnableLambda

def get_formatted_report(topic):
    return RunnableLambda( lambda section: format_report(topic, section))


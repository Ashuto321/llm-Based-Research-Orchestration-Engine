from langchain_core.runnables import RunnableParallel
from chains.section_chain import get_section_chain


def get_parallel_chain(model, topic):
    
    section_chain= get_section_chain(model)
    
    parallel_chain = RunnableParallel({
        "introduction": ({
            "section": lambda x: "introduction",
            "topic": lambda x: topic
        } | section_chain ),
        
        "Applictaion": (
            {
                "section": lambda x: "application",
                "topic": lambda x: topic
            } | section_chain ),
        
        "Challenges": ({
            "section": lambda x: "challenges",
            "topic": lambda x: topic
        } | section_chain )
    })
    
    return parallel_chain





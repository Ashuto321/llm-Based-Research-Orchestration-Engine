from prompts.planner_prompt import planner_prompt

def get_planner_chain(model):
    return planner_prompt | model



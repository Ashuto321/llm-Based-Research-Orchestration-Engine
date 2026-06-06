from prompts.section_prompt import section_prompt

def get_section_chain(model):
    return section_prompt | model
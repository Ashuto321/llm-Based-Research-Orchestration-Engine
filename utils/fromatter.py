# putting output in structured format

def format_report(topic, section):
    
    report = f" {topic} \n\n"
    
    for section_name, content in section.items():
        report += f" {section_name} \n\n"
        report += f"{content.content} + \n\n"
            
    return report



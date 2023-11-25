
from haystack.nodes import PromptTemplate,AnswerParser,PromptNode
api_key = "api_key"

def initialize_prompt_node():
    prompt_template = PromptTemplate(prompt = """"Given the provided Documents, answer the Query. Make your answer detailed and long upto 100 words \n
                                                Query: {query}\n
                                                Documents: {join(documents)}
                                                Answer: 
                                            """,
                                            output_parser=AnswerParser())

    prompt_node = PromptNode(model_name_or_path = "gpt-3.5-turbo",
                            api_key = api_key,
                            max_length=1000,
                            default_prompt_template = prompt_template)
    return prompt_node


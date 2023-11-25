import re
from dbutils import initialize_vectorstore
from preprocessing import data_preprocessing
from Retriever import info_retriever
from document_prompt import initialize_prompt_node
import warnings
from haystack import Pipeline
warnings.filterwarnings("ignore")
import chainlit as cl

# def chatbot():
document_store = initialize_vectorstore()


prompt_node = initialize_prompt_node()


document_store = data_preprocessing(document_store)


retriever = info_retriever(document_store)
document_store.update_embeddings(retriever)

query_pipeline = Pipeline()
query_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
query_pipeline.add_node(component=prompt_node, name="PromptNode", inputs=["Retriever"])
    

@cl.on_message
async def main(message: cl.Message):
    #print(inp_message)
    response = await cl.make_async(query_pipeline.run)(message.content)
    sentences = response['answers'][0].answer.split('\n')

    # Check if the last sentence doesn't end with '.', '?', or '!'
    if sentences and not sentences[-1].strip().endswith(('.', '?', '!')):
        # Remove the last sentence
        sentences.pop()

    result = '\n'.join(sentences[1:])
    await cl.Message(author="Bot", content=result).send()
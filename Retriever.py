from haystack.nodes import EmbeddingRetriever



def info_retriever(document_store):
    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/all-MiniLM-L6-v2"
    )

    return retriever
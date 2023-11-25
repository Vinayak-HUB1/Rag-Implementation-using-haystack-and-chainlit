
from haystack.document_stores import WeaviateDocumentStore




def initialize_vectorstore():
    document_store = WeaviateDocumentStore(
        host='http://localhost',
        port=8080,
        embedding_dim=384
    )
    return document_store
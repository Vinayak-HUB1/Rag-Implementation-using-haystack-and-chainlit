
from haystack.nodes import TextConverter, PreProcessor



def data_preprocessing(document_store):
    converter = TextConverter(remove_numeric_tables=True, valid_languages=["en"])
    #doc_txt1 = converter.convert(file_path="ai.txt", meta=None)[0]
    doc_txt2 = converter.convert(file_path="cv.txt", meta=None)[0]
    doc_txt3 = converter.convert(file_path="nlp.txt", meta=None)[0]
    doc_txt4 = converter.convert(file_path="ml.txt", meta=None)[0]




    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=False,
        split_by="word",
        split_length=100,
        split_respect_sentence_boundary=True,
    )
    docs_default = preprocessor.process([doc_txt2,doc_txt3,doc_txt4],split_respect_sentence_boundary=True)

    document_store.write_documents(docs_default)
    return document_store
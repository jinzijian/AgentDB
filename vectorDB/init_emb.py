import langchain
from langchain.embeddings import OpenAIEmbeddings
key = "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"
embeddings_model = OpenAIEmbeddings(openai_api_key=key)

# Todo: 支持多种Embedding; OpenAI; Bge-En; Bge-ZH
def get_embeddings_model(api_key):
    embeddings_model = OpenAIEmbeddings(openai_api_key=api_key)
    return embeddings_model
if __name__=="__main__":
    emb_model = get_embeddings_model(key)
    embeddings = emb_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
    )
    print(len(embeddings), len(embeddings[0]))
    embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
    print(embedded_query[:5])
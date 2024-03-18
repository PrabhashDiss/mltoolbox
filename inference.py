import cohere
import json

def get_llm_answer(api_key, query, model_kwargs=None):
    co = cohere.Client(api_key)
    response = co.chat(
        chat_history=[
            {"role": "USER", "message": "Who discovered gravity?"},
            {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
        ],
        message=query,
        connectors=[{"id": "web-search"}]
    )
    result = json.loads(response.text)
    return result["text"] if result else None

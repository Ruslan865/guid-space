def mock_chatgpt_response(query):
    if "python" in query.lower():
        return "Python-da list [] ilə yaradılır."
    elif "salam" in query.lower():
        return "Salam! Mən buradayam, sən necəsən?"
    return "Bu sual üçün mənim fikrim belədir..."

def mock_claude_response(query):
    return "Claude-un cavabı: " + query.capitalize()

def mock_mistral_response(query):
    return "Mistral-a görə: bu barədə belə düşünmək olar..."

def mock_perplexity_response(query):
    return "Perplexity cavabı: sorğunuzun nəticəsi belədir..."

def analyze_all_responses(query):
    responses = {
        "ChatGPT": mock_chatgpt_response(query),
        "Claude": mock_claude_response(query),
        "Mistral": mock_mistral_response(query),
        "Perplexity": mock_perplexity_response(query)
    }

    for name, resp in responses.items():
        if "Python" in query and "list" in resp:
            return f"(Seçildi: {name})\n{resp}"

    return f"(Bir neçə AI cavabından seçildi)\n{list(responses.values())[0]}"

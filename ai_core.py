from multi_ai_responder import analyze_all_responses
from answer_selector import select_best_answer

def think_like_ai(query, results_dict):
    if query.lower() in ["necəsən", "salam", "xoş gördük", "haradasan", "nə var nə yox"]:
        return "Mən yaxşıyam, sən necəsən, dostum? 😊"

    if results_dict:
        smart_summary = select_best_answer(query, results_dict)
        combined = query + " " + smart_summary
        ai_decision = analyze_all_responses(combined)
        return "Birləşmiş AI cavabı budur, dostum:\n\n" + ai_decision
    else:
        return analyze_all_responses(query)

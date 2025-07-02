import os
import importlib
from flask import Flask, request, jsonify, render_template
from doc_creator import save_to_pdf
from answer_selector import select_best_answer
from multi_ai_responder import analyze_all_responses

app = Flask(__name__)

def is_emotional_question(query):
    emosiyalar = ["salam", "necəsən", "xoş gördük", "nə var nə yox", "halın necədir", "haradasan", "necə gedir"]
    return any(word in query.lower() for word in emosiyalar)

def emotional_response(query):
    variants = [
        "Mən çox yaxşıyam 😊", "Səninlə danışmaq xoşdur! 😄",
        "Salam dostum! Mən hazıram! 🤖", "Bugün enerjim yüksəkdir ⚡"
    ]
    import random
    return random.choice(variants)

def run_search(query):
    scrapers = [f for f in os.listdir('.') if f.startswith("scraper_") and f.endswith(".py")]
    results_dict = {}

    for scraper in scrapers:
        module_name = scraper[:-3]
        try:
            module = importlib.import_module(module_name)
            result = module.search(query)
            if result and isinstance(result, list):
                results_dict[module_name.replace("scraper_", "")] = result
        except Exception as e:
            print(f"Error in {module_name}: {e}")

    final_answer = select_best_answer(query, results_dict)
    save_to_pdf(query, [final_answer])
    return query + " " + final_answer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')

    if not message:
        return jsonify({'reply': 'Sual daxil edin'})

    if is_emotional_question(message):
        return jsonify({'reply': emotional_response(message)})

    enriched = run_search(message)
    final_reply = analyze_all_responses(enriched)

    return jsonify({'reply': final_reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

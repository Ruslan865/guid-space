import os
import importlib
from flask import Flask, request, jsonify, render_template
from doc_creator import save_to_pdf
from answer_selector import select_best_answer

app = Flask(__name__)

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
    return final_answer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    if message:
        answer = run_search(message)
        return jsonify({'reply': answer})
    return jsonify({'reply': 'Sual daxil edin'})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

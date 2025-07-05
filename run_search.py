import os
import importlib
from answer_selector import select_best_answer
from doc_creator import save_to_pdf

def run_search(query):
    scrapers = [f for f in os.listdir('.') if f.startswith("scraper_") and f.endswith(".py")]
    results_dict = {}

    for scraper in scrapers:
        module_name = scraper[:-3]  # remove ".py"
        try:
            module = importlib.import_module(module_name)
            result = module.search(query)
            if result and isinstance(result, list):
                results_dict[module_name.replace("scraper_", "")] = result
        except Exception as e:
            print(f"Error in {module_name}: {e}")

    final_answer = select_best_answer(query, results_dict)
    print("Final cavab:", final_answer)
    save_to_pdf(query, [final_answer])
    return final_answer
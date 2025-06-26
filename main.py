import os
import importlib
from doc_creator import save_to_pdf
from answer_selector import select_best_answer

def run_search(query):
    scrapers = [f for f in os.listdir('.') if f.startswith("scraper_") and f.endswith(".py")]
    results_dict = {}

    print("\n🔍 Axtarılır...\n")

    for scraper in scrapers:
        module_name = scraper[:-3]  # remove .py
        try:
            module = importlib.import_module(module_name)
            result = module.search(query)
            if result and isinstance(result, list):
                results_dict[module_name.replace("scraper_", "")] = result
                print(f"✅ {module_name.replace('scraper_', '').capitalize()} nəticəsi:")
                print(f"- {result[0][:100]}...\n" if result[0] else "- Heç nə tapılmadı.\n")
            else:
                print(f"❌ {module_name.replace('scraper_', '').capitalize()} nəticə qaytarmadı.\n")
        except Exception as e:
            print(f"🚫 {module_name.replace('scraper_', '').capitalize()} işlənərkən xəta: {e}\n")

    final_answer = select_best_answer(query, results_dict)
    save_to_pdf(query, [final_answer])
    print("📄 PDF faylı yaradıldı: output.pdf\n")

if __name__ == "__main__":
    while True:
        user_input = input("💬 Sualınızı yazın (və ya 'exit' yazın): ").strip()
        if user_input.lower() == "exit":
            break
        elif user_input:
            run_search(user_input)
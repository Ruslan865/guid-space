def select_best_answer(query, results_dict):
    best = ""
    for key, results in results_dict.items():
        if results:
            best = results[0]
            break
    return best if best else "Məlumat tapılmadı."

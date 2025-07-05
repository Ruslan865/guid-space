def select_best_answer(query, results_dict):
    for source, answers in results_dict.items():
        if answers:
            return f"{source} nəticəsi: {answers[0]}"
    return "Nəticə tapılmadı."

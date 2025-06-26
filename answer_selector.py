import re

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())

def extract_keywords(query):
    stop_words = {"nədir", "necə", "niyə", "haqqında", "və", "ya", "bir", "üçün", "ilə"}
    words = clean_text(query).split()
    return [w for w in words if w not in stop_words]

def clean_answer_text(text):
    # Emojiləri sadə simvollara dəyişir
    replacements = {
        "📌": "[!]",
        "❗": "[!]",
        # Lazım gələrsə başqa simvollar əlavə oluna bilər
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

def select_best_answer(query, results_dict):
    keywords = extract_keywords(query)
    all_answers = []
    for source, answers in results_dict.items():
        for ans in answers:
            all_answers.append((source, ans.strip()))

    scored = []
    for source, answer in all_answers:
        word_list = clean_text(answer).split()
        match_count = sum(1 for word in word_list if word in keywords)
        scored.append((match_count, source, answer))

    scored.sort(reverse=True)
    if scored and scored[0][0] > 0:
        _, source, best = scored[0]
        best = clean_answer_text(best)
        return f"[!] Ən uyğun nəticə ({source}):\n{best}"
    else:
        return "[!] Uyğun nəticə tapılmadı, zəhmət olmasa sualı dəqiqləşdirin."
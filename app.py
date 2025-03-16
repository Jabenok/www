from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/opros.html', methods=['GET', 'POST'])
def opros():
    if request.method == 'POST':
        answers = request.form

        # Обнуляем баллы перед новым тестом
        destinations = {
            "Байкал": 0, "Камчатка": 0, "Алтай": 0,
            "Сочи": 0, "Крым": 0, "Анапа": 0,
            "Санкт-Петербург": 0, "Казань": 0, "Великий Новгород": 0,
            "Астрахань": 0, "Краснодар": 0, "Ростов-на-Дону": 0
        }

        # Анализируем ответы пользователя
        if answers.get("activity") == "active":
            destinations["Байкал"] += 2
            destinations["Камчатка"] += 2
            destinations["Алтай"] += 2
        elif answers.get("activity") == "calm":
            destinations["Сочи"] += 2
            destinations["Крым"] += 2
            destinations["Анапа"] += 2
        elif answers.get("activity") == "cultural":
            destinations["Санкт-Петербург"] += 2
            destinations["Казань"] += 2
            destinations["Великий Новгород"] += 2
        elif answers.get("activity") == "food":
            destinations["Астрахань"] += 2
            destinations["Краснодар"] += 2
            destinations["Ростов-на-Дону"] += 2

        if answers.get("climate") == "cold":
            destinations["Байкал"] += 2
            destinations["Камчатка"] += 2
        elif answers.get("climate") == "warm":
            destinations["Сочи"] += 2
            destinations["Крым"] += 2
        elif answers.get("climate") == "moderate":
            destinations["Казань"] += 2
            destinations["Санкт-Петербург"] += 2

        if answers.get("length") == "short":
            destinations["Казань"] += 2
            destinations["Санкт-Петербург"] += 2
        elif answers.get("length") == "medium":
            destinations["Алтай"] += 2
            destinations["Крым"] += 2
        elif answers.get("length") == "long":
            destinations["Камчатка"] += 2
            destinations["Байкал"] += 2

        if answers.get("transport") == "plane":
            destinations["Камчатка"] += 2
            destinations["Сочи"] += 2
        elif answers.get("transport") == "train":
            destinations["Санкт-Петербург"] += 2
            destinations["Казань"] += 2
        elif answers.get("transport") == "car":
            destinations["Крым"] += 2
            destinations["Краснодар"] += 2
        elif answers.get("transport") == "ship":
            destinations["Астрахань"] += 2
            destinations["Байкал"] += 2

        if answers.get("budget") == "low":
            destinations["Алтай"] += 2
            destinations["Крым"] += 2
        elif answers.get("budget") == "medium":
            destinations["Казань"] += 2
            destinations["Краснодар"] += 2
        elif answers.get("budget") == "high":
            destinations["Сочи"] += 2
            destinations["Камчатка"] += 2

        # Определяем направление с наибольшими баллами
        best_destination = max(destinations, key=destinations.get)

        return render_template("result.html", destination=best_destination)

    return render_template("opros.html")

if __name__=='__main__':
    app.run(debug=True)
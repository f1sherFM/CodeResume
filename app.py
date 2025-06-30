from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Конфигурация
app.config.update(
    ENV='production',
    SERVER_NAME=None,
)

# Данные о себе
ABOUT_ME = """
Привет! Я — Python-разработчик. Призёр многих онлайн-олимпиад, победитель в IT-хакатоне в номинации "Лучший Код"
Занял 2 место на чемпионате "Профессионалы". Делал работы для таких известных компаний как: "Kaspersky" и "Sber-Tech".
Специализируюсь в таких направлениях как: Data Science и Machine Learning. Занимаюсь питоном 2 года.
Год занимался в It-Cube г. Сургута, в недавном времени забрали Кубок на "Кубитве".
"""

# Список задач Codewars
CODEWARS_SOLUTIONS = [
    {
        "id": "multiply",
        "title": "Multiply",
        "description": "Напишите функцию, которая умножает два числа.",
        "link": "https://www.codewars.com/kata/50654ddff44f800200000004",
        "test_cases": "# Should return 6\nmultiply(2, 3)\n\n# Should handle zeros\nmultiply(5, 0)\n\n# Should work with negatives\nmultiply(-2, 4)",
        "kyu": "8kyu",
        "added_date": "2025-06-28"
    },
    {
        "id": "even_or_odd",
        "title": "Even or Odd",
        "description": "Определите, является ли число чётным или нечётным.",
        "link": "https://www.codewars.com/kata/53da3dbb4a5168369a0000fe",
        "test_cases": "# Should return 'Even'\neven_or_odd(4)\n\n# Should return 'Odd'\neven_or_odd(7)\n\n# Should handle zero\neven_or_odd(0)",
        "kyu": "8kyu",
        "added_date": "2025-06-28"
    },
    {
        "id": "sum_of_positive",
        "title": "Sum of Positive",
        "description": "Верните сумму положительных чисел в массиве.",
        "link": "https://www.codewars.com/kata/5715eaedb436cf5606000381",
        "test_cases": "# Should return 15\npositive_sum([1, 2, 3, 4, 5])\n\n# Should return 0 for empty array\npositive_sum([])\n\n# Should ignore negative numbers\npositive_sum([-1, 2, -3, 4, -5])",
        "kyu": "8kyu",
        "added_date": "2025-06-39"
    },
    {
        "id": "vowel_count",
        "title": "Vowel Count",
        "description": "Верните количество гласных в переданной строке.",
        "link": "https://www.codewars.com/kata/54ff3102c1bad923760001f3",
        "test_cases": "# Should return 5\nvowel_count('abracadabra')\n\n# Should return 0\nvowel_count('my pyx')\n\n# Should work with uppercase\nvowel_count('AEIOU')",
        "kyu": "7kyu",
        "added_date": "2025-06-29"
    },
    {
        "id": "disemvowel_trolls",
        "title": "Disemvowel Trolls",
        "description": "Удалите все гласные из строки.",
        "link": "https://www.codewars.com/kata/52fba66badcd10859f00097e",
        "test_cases": "# Should return 'Ths wbst s fr lsrs LL!'\ndisemvowel('This website is for losers LOL!')\n\n# Should handle empty string\ndisemvowel('')\n\n# Should work with mixed case\ndisemvowel('No offense but,\\nYour writing is terrible.')",
        "kyu": "7kyu",
        "added_date": "2025-06-29"
    },
    {
        "id": "return_negative",
        "title": "Return Negative",
        "description": "Верните отрицательное число для любого положительного, иначе верните само число.",
        "link": "https://www.codewars.com/kata/55685cd7ad70877c23000102",
        "test_cases": "# Should return -1\nmake_negative(1)\n\n# Should return -5\nmake_negative(-5)\n\n# Should return 0\nmake_negative(0)",
        "kyu": "8kyu",
        "added_date": "2025-06-29"
    },
    {
        "id": "reversed_strings",
        "title": "Reversed Strings",
        "description": "Переверните переданную строку.",
        "link": "https://www.codewars.com/kata/5168bb5dfe9a00b126000018",
        "test_cases": "# Should return 'dlrow'\nsolution('world')\n\n# Should return ''\nsolution('')\n\n# Should work with single character\nsolution('a')",
        "kyu": "8kyu",
        "added_date": "2025-06-29"
    },
    {
        "id": "remove_first_last_char",
        "title": "Remove First and Last Character",
        "description": "Удалите первый и последний символ из строки.",
        "link": "https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0",
        "test_cases": "# 'eloquent' => 'loquen'\nremove_char('eloquent')\n# 'country' => 'ountr'\nremove_char('country')",
        "kyu": "8kyu",
        "added_date": "2025-06-30"
    },
    {
        "id": "string_repeat",
        "title": "String repeat",
        "description": "Повторите строку указанное количество раз.",
        "link": "https://www.codewars.com/kata/57a0e5c372292dd76d000d7e",
        "test_cases": "# 3, 'hi' => 'hihihi'\nrepeat_str(3, 'hi')\n# 5, 'Hello' => 'HelloHelloHelloHelloHello'",
        "kyu": "8kyu",
        "added_date": "2025-06-30"
    },
    {
        "id": "multiples_of_3_or_5",
        "title": "Multiples of 3 or 5",
        "description": "Найдите сумму всех чисел, кратных 3 или 5 ниже переданного числа.",
        "link": "https://www.codewars.com/kata/514b92a657cdc65150000006",
        "test_cases": "# 10 => 23 (3+5+6+9)\nsolution(10)\n# 20 => 78 (3+5+6+9+10+12+15+18)",
        "kyu": "6kyu",
        "added_date": "2023-06-30"
    }
]

# Сортировка по дате (новые сверху)
CODEWARS_SOLUTIONS.sort(key=lambda x: x['added_date'], reverse=True)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route("/")
def home():
    skills = {
        "Core": [
            {"name": "Python", "level": "Advanced", "icon": "fab fa-python"},
            {"name": "Flask", "level": "Advanced", "icon": "fas fa-flask"}
        ],
        "Data Science": [
            {"name": "pandas", "level": "Proficient", "icon": "fas fa-table"},
            {"name": "numpy", "level": "Proficient", "icon": "fas fa-calculator"},
            {"name": "Other DS/ML stack", "level": "Experienced", "icon": "fas fa-brain"}
        ]
    }
    
    return render_template(
        "index.html",
        name="Балуков Кирилл",
        bio="Python Developer | Data Scientist",
        about_me=ABOUT_ME,
        skills=skills,
        solutions=CODEWARS_SOLUTIONS
    )

@app.route("/codewars/<solution_id>")
def show_solution(solution_id):
    solution = next((s for s in CODEWARS_SOLUTIONS if s["id"] == solution_id), None)
    if not solution:
        return "Решение не найдено", 404
    
    next_index = (CODEWARS_SOLUTIONS.index(solution) + 1) % len(CODEWARS_SOLUTIONS)
    next_solution = CODEWARS_SOLUTIONS[next_index]
    
    try:
        with open(f"static/solutions/{solution_id}.txt", "r") as f:
            code = f.read()
    except FileNotFoundError:
        code = "Решение пока не добавлено"
    
    return render_template(
        f"codewars/{solution_id}.html",
        title=solution["title"],
        description=solution["description"],
        link=solution["link"],
        code=code,
        test_cases=solution["test_cases"],
        next_solution=next_solution,
        kyu=solution.get("kyu", ""),
        added_date=solution.get("added_date", "")
    )

if __name__ != '__main__':
    app.run(host='0.0.0.0', port=5001)
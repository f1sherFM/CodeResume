from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

# Конфигурация приложения
app.config.update(
    ENV='production',
    SERVER_NAME=None,
    TEMPLATES_AUTO_RELOAD=True
)

# Данные о себе
ABOUT_ME = """
Привет! Я — Python-разработчик. Призёр многих онлайн-олимпиад, победитель в IT-хакатоне в номинации "Лучший Код".
Занял 2 место на чемпионате "Профессионалы". Делал работы для таких известных компаний как: "Kaspersky" и "Sber-Tech".
Специализируюсь в таких направлениях как: Data Science и Machine Learning. Занимаюсь питоном 2 года.
Год занимался в It-Cube г. Сургута, в недавном времени забрали Кубок на "Кубитве".
"""

# Полный список задач Codewars
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
        "id": "square_sum",
        "title": "Square(n) Sum",
        "description": "Возведите в квадрат каждый элемент массива и суммируйте результаты.",
        "link": "https://www.codewars.com/kata/515e271a311df0350d00000f",
        "test_cases": "# Should return 5\nsquare_sum([1, 2])\n\n# Should return 50\nsquare_sum([0, 3, 4, 5])\n\n# Should return 0\nsquare_sum([])",
        "kyu": "8kyu",
        "added_date": "2025-07-02"
    },
    {
        "id": "duplicate_encoder",
        "title": "Duplicate Encoder",
        "description": "Преобразуйте строку, заменяя символы на '(' если они встречаются один раз и ')' если повторяются.",
        "link": "https://www.codewars.com/kata/54b42f9314d9229fd6000d9c",
        "test_cases": "# Should return '((('\nduplicate_encoder('din')\n\n# Should return '()()()'\nduplicate_encoder('recede')\n\n# Should return ')())())'\nduplicate_encoder('Success')",
        "kyu": "6kyu",
        "added_date": "2025-07-02"
    },
    {
        "id": "sum_two_smallest",
        "title": "Sum of two lowest positive integers",
        "description": "Найдите сумму двух наименьших положительных чисел в массиве.",
        "link": "https://www.codewars.com/kata/558fc85d8fd1938afb000014",
        "test_cases": "# Should return 7\nsum_two_smallest_numbers([5, 8, 12, 18, 22])\n\n# Should return 3453455\nsum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])",
        "kyu": "7kyu",
        "added_date": "2025-07-02"
    },
    {
        "id": "to_camel_case",
        "title": "Convert string to camel case",
        "description": "Преобразуйте строки с разделителями '-' или '_' в camelCase.",
        "link": "https://www.codewars.com/kata/517abf86da9663f1d2000003",
        "test_cases": "# Should return 'theStealthWarrior'\nto_camel_case('the-stealth-warrior')\n\n# Should return 'TheStealthWarrior'\nto_camel_case('The_Stealth_Warrior')",
        "kyu": "6kyu",
        "added_date": "2025-07-02"
    },
    {
        "id": "friend_or_foe",
        "title": "Friend or Foe?",
        "description": "Отфильтруйте массив строк, оставив только строки длиной 4 символа.",
        "link": "https://www.codewars.com/kata/55b42574ff091733d900002f",
        "test_cases": "# Should return ['Ryan', 'Mark']\nfriend(['Ryan', 'Kieran', 'Mark'])\n\n# Should return []\nfriend(['Jimm', 'Cari', 'aret'])",
        "kyu": "7kyu",
        "added_date": "2025-07-02"
    },
    {
        "id": "tribonacci",
        "title": "Tribonacci Sequence",
        "description": "Реализуйте последовательность Трибоначчи (аналог Фибоначчи, но каждый элемент - сумма трех предыдущих).",
        "link": "https://www.codewars.com/kata/556deca17c58da83c00002db",
        "test_cases": "# Should return [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]\ntribonacci([1, 1, 1], 10)\n\n# Should return [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]\ntribonacci([0, 0, 1], 10)",
        "kyu": "6kyu",
        "added_date": "2025-07-02"
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
        "added_date": "2025-06-29"
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
        "added_date": "2025-06-30"
    },
    {
        "id": "find_smallest_int",
        "title": "Find the smallest integer in the array",
        "description": "Найдите наименьшее целое число в массиве.",
        "link": "https://www.codewars.com/kata/55a2d7ebe362935a210000b2",
        "test_cases": "# Should return -345\nfind_smallest_int([34, -345, -1, 100])\n\n# Should return 8\nfind_smallest_int([8, 10, 15, 20])",
        "kyu": "8kyu",
        "added_date": "2025-07-01"
    },
    {
        "id": "summation",
        "title": "Grasshopper - Summation",
        "description": "Найдите сумму всех чисел от 1 до n.",
        "link": "https://www.codewars.com/kata/55d24f55d7dd296eb9000030",
        "test_cases": "# Should return 36\nsummation(8)\n\n# Should return 1\nsummation(1)\n\n# Should return 55\nsummation(10)",
        "kyu": "8kyu",
        "added_date": "2025-07-01"
    },
    {
        "id": "mumbling",
        "title": "Mumbling",
        "description": "Преобразуйте строку по определенному шаблону (каждая буква повторяется n раз).",
        "link": "https://www.codewars.com/kata/5667e8f4e3f572a8f2000039",
        "test_cases": "# Should return 'A-Bb-Ccc-Dddd'\naccum('abcd')\n\n# Should return 'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'\naccum('RqaEzty')",
        "kyu": "7kyu",
        "added_date": "2025-07-01"
    },
    {
        "id": "jaden_casing",
        "title": "Jaden Casing Strings",
        "description": "Преобразуйте строку так, чтобы каждое слово начиналось с заглавной буквы.",
        "link": "https://www.codewars.com/kata/5390bac347d09b7da40006f6",
        "test_cases": "# Should return 'How Can Mirrors Be Real If Our Eyes Aren't Real'\nto_jaden_case('How can mirrors be real if our eyes aren't real')",
        "kyu": "7kyu",
        "added_date": "2025-07-01"
    }
]

# Сортировка по дате (новые сверху)
CODEWARS_SOLUTIONS.sort(key=lambda x: x['added_date'], reverse=True)

# Обработчики ошибок
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Функция для получения навыков
def get_skills():
    return {
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

# Главная страница
@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Балуков Кирилл",
        bio="Python Developer | Data Scientist",
        about_me=ABOUT_ME,
        skills=get_skills(),
        solutions=CODEWARS_SOLUTIONS,
        active_filter="all"
    )

# Фильтрация задач
@app.route("/codewars/filter")
def filter_solutions():
    kyu_filter = request.args.get('kyu')
    date_filter = request.args.get('date')
    
    filtered_solutions = CODEWARS_SOLUTIONS
    
    # Фильтрация по уровню kyu
    if kyu_filter:
        filtered_solutions = [s for s in filtered_solutions if s['kyu'] == kyu_filter]
    
    # Фильтрация по дате
    if date_filter:
        filtered_solutions = [s for s in filtered_solutions if s['added_date'] >= date_filter]
    
    return render_template(
        "index.html",
        name="Балуков Кирилл",
        bio="Python Developer | Data Scientist",
        about_me=ABOUT_ME,
        skills=get_skills(),
        solutions=filtered_solutions,
        active_filter=kyu_filter if kyu_filter else "date" if date_filter else "all"
    )

# Страница решения задачи
@app.route("/codewars/<solution_id>")
def show_solution(solution_id):
    # Поиск решения по ID
    solution = next((s for s in CODEWARS_SOLUTIONS if s["id"] == solution_id), None)
    
    if not solution:
        return "Решение не найдено", 404
    
    # Получение следующей задачи для навигации
    current_index = CODEWARS_SOLUTIONS.index(solution)
    next_index = (current_index + 1) % len(CODEWARS_SOLUTIONS)
    next_solution = CODEWARS_SOLUTIONS[next_index]
    
    # Чтение кода решения из файла
    try:
        with open(f"static/solutions/{solution_id}.txt", "r", encoding='utf-8') as f:
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

# Запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    app.run(host='0.0.0.0', port=5001)
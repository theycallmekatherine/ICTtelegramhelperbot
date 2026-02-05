import telebot
from telebot import types
import pymysql
import time

bot = telebot.TeleBot("8565209024:AAH5KXOX1c9DZGFSD-BUi6FQTbA4Uwqtjos")

user_state = {}
ege_data = {
    "1": "📊 **ЗАДАНИЕ 1: АНАЛИЗ ГРАФОВ**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Умение сопоставлять таблицу и схему дорог.\n"
         "🧠 **Что знать:** Весовые матрицы и поиск кратчайших путей.\n",

    "2": "⚖️ **ЗАДАНИЕ 2: ТАБЛИЦЫ ИСТИННОСТИ**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Построение и анализ логических выражений.\n"
         "🧠 **Что знать:** И, ИЛИ, НЕ, Импликация (->), Эквивалентность (≡).\n",

    "3": "🗄️ **ЗАДАНИЕ 3: БАЗЫ ДАННЫХ**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Поиск информации в реляционных таблицах.\n"
         "🧠 **Что знать:** Фильтры Excel, работа с ID и связями таблиц.\n",

    "4": "🔐 **ЗАДАНИЕ 4: УСЛОВИЕ ФАНО**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Однозначное декодирование и кратчайший код.\n"
         "🧠 **Что знать:** Построение двоичных деревьев.\n",

    "5": "⚙️ **ЗАДАНИЕ 5: АЛГОРИТМЫ**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Анализ алгоритмов для формальных исполнителей.\n"
         "🧠 **Что знать:** Двоичная система, побитовые операции.\n",

    "6": "🐢 **ЗАДАНИЕ 6: ЧЕРЕПАХА**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Анализ геометрии на плоскости.\n"
         "🧠 **Что знать:** Циклы в Python/Кумире, расчет площади фигур.\n",

    "7": "📸 **ЗАДАНИЕ 7: МУЛЬТИМЕДИА**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Кодирование звука и изображений.\n"
         "🧠 **Что знать:** Формула I = v * i * t, расчет палитры и битрейта.\n",

    "8": "🔢 **ЗАДАНИЕ 8: КОМБИНАТОРИКА**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Подсчет количества вариантов слов или чисел.\n"
         "🧠 **Что знать:** Перестановки, сочетания, библиотека itertools.\n",

    "9": "📗 **ЗАДАНИЕ 9: ТАБЛИЦЫ EXCEL**\n"
         "━━━━━━━━━━━━━━━━━\n"
         "📝 **Тема:** Обработка данных с помощью функций СРЗНАЧ, ЕСЛИ, СЧЁТ.\n"
         "🧠 **Что знать:** Логические условия в строках таблиц.\n",

    "10": "🔎 **ЗАДАНИЕ 10: ПОИСК В ТЕКСТЕ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Работа с текстовым процессором (Word).\n"
          "🧠 **Что знать:** Навигация, поиск целых слов и словоформ.\n",

    "11": "💾 **ЗАДАНИЕ 11: ОБЪЕМ ПАМЯТИ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Расчет веса паролей и идентификаторов.\n"
          "🧠 **Что знать:** Алфавитный подход к расчету веса символа.\n",

    "12": "📝 **ЗАДАНИЕ 12: РЕДАКТОР**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Анализ алгоритмов замены в строках.\n"
          "🧠 **Что знать:** Цикл 'ПОКА', условия 'НАШЛОСЬ'.\n",

    "13": "🌐 **ЗАДАНИЕ 13: IP-СЕТИ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Расчет масок и адресов подсетей.\n"
          "🧠 **Что знать:** Поразрядная конъюнкция, двоичное представление IP.\n",

    "14": "🔢 **ЗАДАНИЕ 14: СИСТЕМЫ СЧИСЛЕНИЯ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Арифметика в различных системах.\n"
          "🧠 **Что знать:** Перевод в любую систему через цикл while.\n",

    "15": "📐 **ЗАДАНИЕ 15: ЛОГИКА (ОТРЕЗКИ/ДЕЛИТЕЛИ)**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Истинность логического выражения.\n"
          "🧠 **Что знать:** Законы логики и программный перебор параметра А.\n",

    "16": "🔄 **ЗАДАНИЕ 16: РЕКУРСИЯ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Вычисление рекурсивных функций.\n"
          "🧠 **Что знать:** Написание рекурсии на Python, кэширование (memoization).\n",

    "17": "📋 **ЗАДАНИЕ 17: ПОСЛЕДОВАТЕЛЬНОСТИ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Обработка списков чисел из файла.\n"
          "🧠 **Что знать:** Работа с циклами, условиями и чтение из .txt.\n",

    "18": "🤖 **ЗАДАНИЕ 18: РОБОТ В EXCEL**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Поиск оптимального пути роботом.\n"
          "🧠 **Что знать:** Динамическое программирование в таблицах.\n",

    "19": "🎮 **ЗАДАНИЕ 19: ТЕОРИЯ ИГР (1 ШАГ)**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Определение выигрышного первого хода.\n"
          "🧠 **Что знать:** Дерево игры, минимальное S для победы.\n",

    "20": "🎮 **ЗАДАНИЕ 20: ТЕОРИЯ ИГР (2 ШАГА)**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Стратегия победы первым или вторым ходом.\n"
          "🧠 **Что знать:** Построение выигрышных стратегий.\n",

    "21": "🎮 **ЗАДАНИЕ 21: ТЕОРИЯ ИГР (ФИНАЛ)**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Гарантированная победа при любой игре противника.\n"
          "🧠 **Что знать:** Использование универсального кода на Python.\n",

    "22": "⏳ **ЗАДАНИЕ 22: ПРОЦЕССЫ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Анализ параллельных вычислений.\n"
          "🧠 **Что знать:** Диаграммы Ганта, расчет времени зависимости процессов.\n",

    "23": "🛤️ **ЗАДАНИЕ 23: ТРАЕКТОРИИ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Количество путей от числа к числу.\n"
          "🧠 **Что знать:** Простая динамика или рекурсия.\n",

    "24": "🔤 **ЗАДАНИЕ 24: СТРОКИ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Обработка длинных символьных строк.\n"
          "🧠 **Что знать:** Методы .replace(), .split(), работа с циклами.\n",

    "25": "🎭 **ЗАДАНИЕ 25: МАСКИ ЧИСЕЛ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Поиск чисел по шаблону и делителям.\n"
          "🧠 **Что знать:** Модуль fnmatch, эффективный поиск делителей.\n",

    "26": "📦 **ЗАДАНИЕ 26: ЖАДНЫЕ АЛГОРИТМЫ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Обработка больших данных (файлы по 10к строк).\n"
          "🧠 **Что знать:** Сортировка, выбор оптимальных пар.\n",

    "27": "🏆 **ЗАДАНИЕ 27: ВЫСШИЙ ПИЛОТАЖ**\n"
          "━━━━━━━━━━━━━━━━━\n"
          "📝 **Тема:** Оптимальная обработка числовых последовательностей.\n"
          "🧠 **Что знать:** Динамика, префиксные суммы, остатки от деления.\n"
}
ege_links = {
    "1": "https://inf-ege.sdamgia.ru/test?theme=357",
    "2": "https://inf-ege.sdamgia.ru/test?theme=352",
    "3": "https://inf-ege.sdamgia.ru/test?theme=424",
    "4": "https://inf-ege.sdamgia.ru/test?theme=369",
    "5": "https://inf-ege.sdamgia.ru/test?theme=362",
    "6": "https://inf-ege.sdamgia.ru/test?theme=316",
    "7": "https://inf-ege.sdamgia.ru/test?theme=250",
    "8": "https://inf-ege.sdamgia.ru/test?theme=243",
    "9": "https://inf-ege.sdamgia.ru/test?theme=406",
    "10": "https://inf-ege.sdamgia.ru/test?theme=410",
    "11": "https://inf-ege.sdamgia.ru/test?theme=350",
    "12": "https://inf-ege.sdamgia.ru/test?theme=356",
    "13": "https://inf-ege.sdamgia.ru/test?theme=254",
    "14": "https://inf-ege.sdamgia.ru/test?theme=247",
    "15": "https://inf-ege.sdamgia.ru/test?theme=233",
    "16": "https://inf-ege.sdamgia.ru/test?theme=275",
    "17": "https://inf-ege.sdamgia.ru/test?theme=423",
    "18": "https://inf-ege.sdamgia.ru/test?theme=412",
    "19": "https://inf-ege.sdamgia.ru/test?theme=407",
    "20": "https://inf-ege.sdamgia.ru/test?theme=408",
    "21": "https://inf-ege.sdamgia.ru/test?theme=409",
    "22": "https://inf-ege.sdamgia.ru/test?theme=215",
    "23": "https://inf-ege.sdamgia.ru/test?theme=183",
    "24": "https://inf-ege.sdamgia.ru/test?theme=413",
    "25": "https://inf-ege.sdamgia.ru/test?theme=414",
    "26": "https://inf-ege.sdamgia.ru/test?theme=415",
    "27": "https://inf-ege.sdamgia.ru/test?theme=416",
}
ege_trena = {
    "1": "https://ctege.info/informatika-teoriya-ege/zadanie-1-ege-po-informatike.html",
    "2": "https://ctege.info/informatika-teoriya-ege/zadanie-2-ege-po-informatike.html",
    "3": "https://ctege.info/informatika-teoriya-ege/zadanie-3-ege-po-informatike.html",
    "4": "https://ctege.info/informatika-teoriya-ege/zadanie-4-ege-po-informatike.html",
    "5": "https://ctege.info/informatika-teoriya-ege/zadanie-5-ege-po-informatike.html",
    "6": "https://ctege.info/informatika-teoriya-ege/zadanie-6-ege-po-informatike.html",
    "7": "https://ctege.info/informatika-teoriya-ege/zadanie-7-ege-po-informatike.html",
    "8": "https://ctege.info/informatika-teoriya-ege/zadanie-8-ege-po-informatike.html",
    "9": "https://ctege.info/informatika-teoriya-ege/zadanie-9-ege-po-informatike.html",
    "10": "https://ctege.info/informatika-teoriya-ege/zadanie-10-ege-po-informatike.html",
    "11": "https://ctege.info/informatika-teoriya-ege/zadanie-11-ege-po-informatike.html",
    "12": "https://ctege.info/informatika-teoriya-ege/zadanie-12-ege-po-informatike.html",
    "13": "https://ctege.info/informatika-teoriya-ege/zadanie-13-ege-po-informatike.html",
    "14": "https://ctege.info/informatika-teoriya-ege/zadanie-14-ege-po-informatike.html",
    "15": "https://ctege.info/informatika-teoriya-ege/zadanie-15-ege-po-informatike.html",
    "16": "https://ctege.info/informatika-teoriya-ege/zadanie-16-ege-po-informatike.html",
    "17": "https://ctege.info/informatika-teoriya-ege/zadanie-17-ege-po-informatike.html",
    "18": "https://ctege.info/informatika-teoriya-ege/zadanie-18-ege-po-informatike.html",
    "19": "https://ctege.info/informatika-teoriya-ege/zadanie-19-ege-po-informatike.html",
    "20": "https://ctege.info/informatika-teoriya-ege/zadanie-20-ege-po-informatike.html",
    "21": "https://ctege.info/informatika-teoriya-ege/zadanie-21-ege-po-informatike.html",
    "22": "https://ctege.info/informatika-teoriya-ege/zadanie-22-ege-po-informatike.html",
    "23": "https://ctege.info/informatika-teoriya-ege/zadanie-23-ege-po-informatike.html",
    "24": "https://ctege.info/informatika-teoriya-ege/zadanie-24-ege-po-informatike.html",
    "25": "https://ctege.info/informatika-teoriya-ege/zadanie-25-ege-po-informatike.html",
    "26": "https://ctege.info/informatika-teoriya-ege/zadanie-26-ege-po-informatike.html",
    "27": "https://ctege.info/informatika-teoriya-ege/zadanie-27-ege-po-informatike.html",
}
ege_video = {
    "1": "https://youtu.be/ayVxU_1SR9A?si=Krc6uespZKL7PIc9",
    "2": "https://youtu.be/WumacIajF50?si=Tpdv4_d9itWPCdVF",
    "3": "https://youtu.be/s0CJHGcoAUc?si=pKL_9ZRSacudhHbq",
    "4": "https://youtu.be/Pdic-7lSIMA?si=_UjZLd8RN7fN65m6",
    "5": "https://youtu.be/mz8pINlcCUk?si=QmIIwF2LOjW7kkSt",
    "6": "https://youtu.be/x3zC3uTHq7w?si=cGLx05BeaeH_2MB6",
    "7": "https://youtu.be/TaG0EpWBX_c?si=Hf6pT4JmPhKnrVtY",
    "8": "https://youtu.be/pM_2ktQZtqw?si=DAEZsEpiaCCl5QPt",
    "9": "https://youtu.be/f7ehZL_BFOA?si=AXV4bAbDgr6fcdUt",
    "10": "https://www.youtube.com/live/BKYXK9q7OmE?si=eAxZ2T8o5fgEqZ9y",
    "11": "https://youtu.be/tZaiHxxiWxM?si=vwcSdq5c9-fyaPeA",
    "12": "https://youtu.be/GkC-8sgIwgE?si=469u6JyMEu_KRji-",
    "13": "https://youtu.be/mOAkDKakInk?si=Rj6Wmau4dvfVo2CE",
    "14": "https://youtu.be/aSGyYZ5gVXc?si=0LP-1q0ejUPOQbRq",
    "15": "https://youtu.be/_QimifoBkzU?si=dcrNEOjGOz-USXoI",
    "16": "https://inf-ege.sdamgia.ru/test?theme=275",
    "17": "https://youtu.be/pSUgdABpcB8?si=A6zCbcugyHQDE2w-",
    "18": "https://youtu.be/DCAYk_3J7No?si=PLre7ZFcQKslWZ3D",
    "19": "https://youtu.be/ZOzZh_-fW8U?si=P3hAFpvJUwE-NegD",
    "20": "https://youtu.be/ZOzZh_-fW8U?si=P3hAFpvJUwE-NegD",
    "21": "https://youtu.be/ZOzZh_-fW8U?si=P3hAFpvJUwE-NegD",
    "22": "https://youtu.be/i4B97ZSBQd0?si=q-37HEwtOIwaV6Sm",
    "23": "https://youtu.be/N0oaDdkBzho?si=2ZyDuJMOWNX8d3pL",
    "24": "https://youtu.be/vOMP-Jdz4Nk?si=mzoBw2z2EM3W4FsS",
    "25": "https://youtu.be/8YzqyCcPKgY?si=EpNyAnvvS2El5mFk",
    "26": "https://youtu.be/g6V94A2r6nM?si=WB02xcawmgkt0IZm",
    "27": "https://youtu.be/iMcX5JGNzAU?si=WAiN0IZlm4UifWGd",
}


def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add( "🙊 Варианты", "📚 Задания ")
    markup.add("❓ Помощь", "‼️ Критерии")
    markup.add("🧿 Тестирование в эмуляторе", "💪 Быстрая тренировка")
    return markup



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет!\nЯ твой помощник ЕГЭ по информатике. 🎓\nПросто введи номер задания (1-27), и я пришлю разборы этого номера и тренировочные варианты. По команде 💪 Быстрая тренировка я пришлю тебе случайное задание. А ещё у меня много интересных функций!",
        reply_markup=main_keyboard()
    )



@bot.message_handler(content_types=["text"])
def handle_text(message):
    chat_id = message.chat.id
    text = message.text.strip()


    if chat_id in user_state:
        correct_answer = user_state[chat_id]["answer"].lower()
        user_answer = text.lower()

        if user_answer == correct_answer:
            bot.send_message(chat_id, "✅ Правильно!")
        else:
            bot.send_message(
                chat_id,
                f"❌ Неправильно\n"
                f"Твой ответ: {text}\n"
                f"Правильный ответ: {correct_answer}"
            )

        del user_state[chat_id]
        return



    if text == "💪 Быстрая тренировка":
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="ege",
            charset="utf8mb4"
        )
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, condition_text, solution_text FROM ege_tasks ORDER BY RAND() LIMIT 1"
        )
        task = cursor.fetchone()
        cursor.close()
        conn.close()

        if not task:
            bot.send_message(chat_id, "⚠️ Нет доступных заданий. Попробуйте позже, когда база обновится")
            return

        task_id, condition, answer = task

        user_state[chat_id] = {
            "task_id": task_id,
            "answer": answer.strip()
        }

        bot.send_message(
            chat_id,
            f"📝 **Вот твоё задание:**\n\n{condition}\n\n"
            f"✏️ Напиши ответ:",
            parse_mode="Markdown"
        )
        return



    if text in ege_data:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🚀 Перейти к практике", url=ege_links[text]))
        markup.add(types.InlineKeyboardButton("📚 Теория по теме", url=ege_trena[text]))
        markup.add(types.InlineKeyboardButton("🎞 Видеоразбор задания", url=ege_video[text]))

        bot.send_message(
            chat_id,
            ege_data[text],
            parse_mode="Markdown",
            reply_markup=markup
        )
        return



    if text == "📚 Задания":
        bot.send_message(chat_id, "📍Введи номер задания от 1 до 27📍", reply_markup=main_keyboard())
        return

    if text == "❓ Помощь":
        bot.send_message(
            chat_id,
            "Бот выдает информацию по номерам ЕГЭ. Просто напиши цифру, например: 1.\nДоступные прототипы заданий в Быстрой тренировке: 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 19, 23",
            reply_markup=main_keyboard()
        )
        return

    if text == "🙊 Варианты":
        bot.send_message(
            chat_id,
            "📝 Перейди по ссылке и решай готовые варианты реального ЕГЭ:\nhttps://kompege.ru/archive",
            reply_markup=main_keyboard()
        )
        return

    if text == "‼️ Критерии":
        with open("shkala-informatika.jpg", "rb") as f:
            bot.send_photo(
                chat_id,
                f,
                caption="🛎 Перевод баллов ЕГЭ по информатике 🛎\n \nПодробные критерии оценивания:\nhttps://inf-ege.sdamgia.ru/manual",
                reply_markup=main_keyboard()
            )
        return

    if text == "🧿 Тестирование в эмуляторе":
        bot.send_message(
            chat_id,
            "🧨 Почувствуй реальный экзамен 🧨:\nhttps://kpolyakov.spb.ru/school/ege/kege/start.htm",
            reply_markup=main_keyboard()
        )
        return



    bot.send_message(
        chat_id,
        "❌ Я не понял сообщение.\n"
        "Введите номер задания от 1 до 27.",
        reply_markup=main_keyboard()
    )


while True:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as e:
        print("[ERROR]", e)
        time.sleep(5)

"""
Case 1
Group:
Uchanov Igor 80%
Fishchukova Sofia 65%
Tsvykh Viktoria 68%
"""

from deep_translator import GoogleTranslator
from textblob import TextBlob

text = input('Введите текст: ')

num_sentences = text.count('.') + text.count('?') + text.count('!')
num_words = len(text.split())


if num_sentences == 0:
    if num_words > 0:
        num_sentences += 1

vovels = "аоуэиыеёяюaeiouy"
syllables = 0
for letter in text.lower():
    if letter in vovels:
        syllables += 1

awl = 0
asl = 0
if num_words == 0:
    awl = syllables
elif num_words > 0:
    awl = syllables / num_words

if num_sentences == 0:
    asl = num_words
elif num_sentences > 0:
    asl = num_words / num_sentences


flash_index = 206.835 - 1.3 * asl - 60.1 * awl
text_hardness = ''
if flash_index > 60:
    if 61 <= flash_index < 80:
        text_hardness = 'Простой язык (Для учеников старших классов)'
    else:
        text_hardness = 'Очень легко читается (Для учеников начальной школы)'
elif flash_index <= 60:
    if 0 <= flash_index < 40:
        text_hardness = 'Очень трудно читать (Для выпускников ВУЗа)'
    else:
        text_hardness = 'Немного трудно читать (Для студентов)'
en = GoogleTranslator(source= 'auto', target = 'en').translate(text)

polarity = TextBlob(en).sentiment.polarity
if polarity >= 0.5:
    polarity = 'Положительно'
elif polarity <= -0.5:
    polarity = "Негативно"
else:
    polarity = "Нейтрально"

subjectivity = f'{round(TextBlob(en).sentiment.subjectivity*100, 1)}%'

res = f"""Предложений: {num_sentences}
Слов: {num_words}
Слогов: {syllables}
Средняя длина предложения в словах: {asl}
Средняя длина слова в слогах: {awl}
Индекс удобочитаемости Флэша: {flash_index}
{text_hardness}
Тональность текста: {polarity}
Объективность: {subjectivity}
"""
print(res)

from textblob import TextBlob


text = 'Я нас росла липа. Липа стала стара. Липа стала суха. Липа упала. Прошли папа и Паша. У папы пила. У Паши топорик. Они распилили липу.'
text = input('')
num_sentences = text.count('.') + text.count('?') + text.count('!')
num_words = len(text.split())

vovels = "аоуэиыеёяюaeiouy"
syllables = 0
for letter in text.lower():
    if letter in vovels:
        syllables += 1

awl = syllables / num_words
asl = num_words / num_sentences

flash_index = 206.835 - 1.3 * asl - 60.1 * awl

if flash_index > 60:
    if 61 <= flash_index < 80:
        print('Простой язык (Для учеников старших классов)')
    else:
        print('Очень легко читается (Для учеников начальной школы)')
elif flash_index <= 60:
    if 0 <= flash_index < 40:
        print('Очень трудно читать (Для выпускников ВУЗа)')
    else:
        print('Немного трудно читать (Для студентов)')


print(TextBlob(text).sentiment)

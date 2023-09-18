"""
Case 1
Group:
Uchanov Igor
Fishchukova Sofia
Tsvykh Viktoria
"""

from deep_translator import GoogleTranslator
from textblob import TextBlob

import ru_local as ru

text = input(ru.INPUT_TEXT)

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
        text_hardness = ru.FLASH_INDEX_1
    else:
        text_hardness = ru.FLASH_INDEX_2
elif flash_index <= 60:
    if 0 <= flash_index < 40:
        text_hardness = ru.FLASH_INDEX_4
    else:
        text_hardness = ru.FLASH_INDEX_3

en = GoogleTranslator(source='auto', target='en').translate(text)

polarity = TextBlob(en).sentiment.polarity

if polarity >= 0.5:
    polarity = ru.POSITIVE_POLARITY
elif polarity <= -0.5:
    polarity = ru.NEGATIVE_POLARITY
else:
    polarity = ru.NEUTRAL_POLARITY

subjectivity = f'{round(TextBlob(en).sentiment.subjectivity * 100, 1)}%'

out = f'''
{ru.SENTENSES} {num_sentences}
{ru.WORDS} {num_words}
{ru.SILLABLES} {syllables}
{ru.ASL} {round(asl, 1)}
{ru.AWL} {round(awl, 1)}
{ru.FLASH_INDEX} {round(flash_index, 1)}
{text_hardness}
{ru.POLARITY} {polarity}
{ru.SUBJECTIVITY} {subjectivity}
'''
print(out)

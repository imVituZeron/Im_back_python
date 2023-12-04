"""
split e join com list e str
split - divide uma string
join - une uma string
strip - tira os caracteres de espaço no começo e no fim
"""

phrase = 'Olha só que, coisa interessante!'
word_list = phrase.split()
core_phrase_list = phrase.split(',')
after_phrase_list = []

for i, phr in enumerate(core_phrase_list):
    after_phrase_list.append(core_phrase_list[i].strip())

print(core_phrase_list)
print(after_phrase_list)

united_phrases = '-'.join(after_phrase_list)
print(united_phrases)

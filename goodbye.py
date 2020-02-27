import random


# I've made one more change in this file
words_list = ('автострада', 'бензин', 'инопланетянин',
             'самолет', 'библиотека', 'шайба', 'олимпиада')

secret_word = random.choice(words_list)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
   letter = input('введите ОДНУ русскую букву: ').lower()
   if len(letter) != 1 or not letter.isalpha():
       continue

   if letter in secret_word:
       for idx, symbol in enumerate(secret_word):
           # print(idx, symbol)
           if letter == symbol:
               gamer_word[idx] = letter
       # if '*' not in gamer_word:
       if gamer_word.count('*') == 0:
           print('вы победили!')
           print('было загадано:', secret_word.upper())
           break
   else:
       # errors_counter = errors_counter + 1
       errors_counter += 1
       print('ошибок допущено:', errors_counter)
       if errors_counter == 8:
           print('вы проиграли :(')
           break
   print(''.join(gamer_word))

print('пробуйте еще')
from random import choice

animes = [['naruto', 'haikyuu', 'obito', 'hanuta'],
     ['pepehype', 'sports', 'shorts', 'series'],
     ['mushishi', 'chill', 'jigara', 'hanuta'],
     ['life', 'forever', 'jigara', 'shorts']]


print('what mood are you in?')
mood = input()

for item in animes:
    if item[1] == mood:
        print(mood + ' anime: ' + item[0])


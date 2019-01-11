text_from = open('questions').readlines()
text_to   = open('answers').readlines()

size = min(len(text_from), len(text_to))

sav = open('res.txt', 'w')

for i in range(size):
    sav.write('' +text_from[i]+'')
    sav.write('' +text_to[i]+'')
    
sav.close
    

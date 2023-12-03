text = open("in.txt",encoding="utf-8").read()

rez = [word for word in text.split() if word[0]==('А')]

with open('out.txt', 'w') as file:
    file.write(str(len(rez)))

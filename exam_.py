a = open(r'test1.txt')
b = open('words.txt', 'w')
c = open('sentence.txt', 'w')
x = a.read()
sent = x.split('.')
words = x.split(' ')
sentence = set(sent)
words1 = set(words)
print(len(sentence))

print(len(words1))
try:
    for i in words1:
        b.write(i)
    for i in sentence:
        c.write(i)
except:
    print("Error")
else:
    print("No Error")
finally:
    a.close()
    b.close()
    c.close()

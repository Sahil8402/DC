a = input("Enter a string:")
words = list(a)
list = []

for i in range(len(words)):
    word = a[-1] + a[:-1]
    new = ''.join(word)
    a = new
    list.append(new)
    i += 1
print(list)

sort = sorted(list)
print(sort)

for i in range(len(words)):
    element = sort[i]
    last = element[- 1]
    i = i + 1
    print(last)
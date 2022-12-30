word = input()
n = int(input())

repeat_words = lambda a, b: a*b

result = repeat_words(word, n)
print(result)
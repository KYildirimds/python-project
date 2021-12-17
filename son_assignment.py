input1 = input('Please write a sentence to see the numbers of chars in your sentence  :')   
dict_sonuc = dict(zip(input1, list(map(lambda x : input1.count(x), input1))))
print(dict_sonuc)
# write a python script to concatenate following dictionaries to create a new one

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic_concate = {}
dic_concate.update(dic1)
dic_concate.update(dic2)
dic_concate.update(dic3)
print(dic_concate)

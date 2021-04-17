# Program Menggunakan Fungsi String

#find
str = "Alica Ayu Fitriani"
print("str: " + str)
print('str find i = ', str.find('i'))
print('str find y = ', str.find('y'))
print('str find t = ', str.find('t'))

#count
print ('jumlah huruf i = ', str.count('i'))
print ('jumlah huruf y = ', str.count('y'))
print ('jumlah huruf a = ', str.count('a'))

#replace
print('str replace Ayu = ',str.replace("Ayu", "A"))
print('str replace Fitriani = ',str.replace("Fitriani", "F"))
print('str replace Ayu Fitriani = ',str.replace("Ayu Fitriani", "AF"))
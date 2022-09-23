# Вини-Пух ритм есть, если число гласных букв в каждой Фразе одинаковое, 
# если во фразе несколько слов, то они разделяются дефисами
song=(input("Введите текст кричалки: ")).split('-')
print(song)
count = 0
temp1=[]
temp2=[]
vowels = set("aeiou")
for i  in range(0,len(song)):
    for letter in song[i]:
         if letter in vowels:
            count += 1
            temp1.append(count)
if min(temp1)==max(temp1):
    print("ПА рам па па рам па ра рам")
if min(temp1)!=max(temp1): print("ПА рам")
print(f"Количество слогов равно: {count}")
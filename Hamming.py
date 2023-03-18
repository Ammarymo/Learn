#Input file 
file = open(input("Your folder"))
file_r= file.read()

#Splitting
list_file = file_r.split("\n")
count = 0

for i, y in zip(list_file[0], list_file[1]):
    if i != y:
        count = count+1
print(count)
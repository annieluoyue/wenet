#生成词典
lang_dict = set() #自动去重

#lang_file.write("<blank> 0" + "\n")
#lang_file.write("<unk> 1" + "\n") 

with open("text.txt","r",encoding="utf-8") as file:
    for item in file.readlines(): #历遍文件夹
        line = item.strip()
        id = line.split(" ")[-1]
        print(id)
        for x in id:
            lang_dict.add(x)
        pass

    pass

print(lang_dict)

lang_file = open("get_dict","w",encoding="utf-8")

#字典的id
count = 2
for i in lang_dict:
    print(i)
    lang_file.write(i+" "+str(count)+"\n")
    count+=1


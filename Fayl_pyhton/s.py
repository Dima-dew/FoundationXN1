import  json   

x  =  {
    "ism" : "Bilmaymiz",
    "familya": "Nomalum",
    "yoshi":  "12"
}


y  =  json.dumps(x)
print(type(y))
# print(y)

with open("inson.json", "w") as f:
    f.write(y)



with open("inson.json", "r") as f1:
    text  = f1.read()
    print(text)


l = json.loads(y)
print(l["yoshi"])
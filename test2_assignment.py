
import sys



with open('haber.txt',encoding='utf-8') as file:
    ff=file.readlines()


lines=[l.strip() for l in ff]
lines2=' '.join(lines)
print('Raw Text:     ',lines2)
def encoder(word,key):
    encoded_data=[]
    for i,x in enumerate(word):
        encoded_data.append(chr(ord(x) + ord(key[i % len(key)])))
    return ''.join(encoded_data)




encoded=encoder(lines2,"alma")
print('Encoded Text: ',encoded)

def decoder(word,key):
    decoded_data=[]
    for i,x in enumerate(word):
        decoded_data.append(chr(ord(x) - ord(key[i % len(key)])))
    return ''.join(decoded_data)

decoded=decoder(encoded,"alma")
print('Decoded Text: ',decoded)



print('''
Second Case
''')

with open(r'haber.txt',encoding='utf-8') as file:
    ff=file.readlines()

lines=[l.strip() for l in ff]
lines2=''.join(lines)
print('Raw Text:     ',lines2)

abc={'a':'@','b':'!','c':'?','d':',','e':'.','f':'*'}

"""
a = @
ş = $
s = 5
i = 1
"""

for i in lines2:
    if i in abc.keys():
        lines2=lines2.replace(i, abc[i])

def encoder(text):
    for i in text:
        if i in abc.keys():
            text=text.replace(i, abc[i])
    return text

encoded=encoder(lines2)
print('Encoded Text: ',encoded)

def decoder(text):
    for i in str(text):
        if i in abc.values():
            text=text.replace(i,list(abc.keys())[list(abc.values()).index(i)])
    return text

decoded=decoder(encoded)
print('Decoded Text: ',decoded)


print('''
Third Case
''')

# with open('haber2.txt',encoding='utf-8') as file:
#     lines=file.readlines()
#
# lines=[l.strip() for l in lines]
line=''.join(lines)

print('Raw Text: ',line)


with open('haber.txt',encoding='utf-8') as file:
    lines=file.readlines()

lines=[l.strip() for l in lines]
line=''.join(lines)

print('Raw Text: ',line)

class Encoder:
    def __init__(self,a, sym, c):
        self.a=a
        self.sym=sym
        self.c=c

    def func_encod(self,new='',new_=''):
        for i in self.a:
            for y in range(len(i)):
                if i[y]==self.sym or (i[y] in self.sym):
                    new+=self.c
                else:
                    new+=i[y]
                new_+=i[y]
        return new,new_

aa=Encoder(line,['a','b','c'],'@')
print("Encoded Text:",aa.func_encod()[0])
print("Decoded Text:",aa.func_encod()[1])

print('''

''')
# class Encoder:
#     def __init__(self,a, sym, c):
#         self.a=a
#         self.sym=sym
#         self.c=c
#
#     def func_encod(self,new=''):
#         for i in self.a:
#             for y in range(len(i)):
#                 if i[y]==self.sym or (i[y] in self.sym):
#                     new+=self.c
#                 else:
#                     new+=i[y]
#                 new_+=i[y]
#         return new
#
# class Decoder(Encoder):
#     def func_decode(self,new=''):
#         for i in self.a:
#             for y in range(len(i)):
#                 if (i[y]==self.c or (i[y] in self.c)) and isinstance(self.sym,list)==False:
#                     new+=self.sym
#                 elif (i[y]==self.c or (i[y] in self.c)) and isinstance(self.sym,list)==True:
#                     for t in self.sym:
#                         new+=t
#                 else:
#                     new+=i[y]
#         return new
#
#
# bb = Decoder(aa.func_encod(),'a','@')
# print("Decoded Text:",bb.func_decode())



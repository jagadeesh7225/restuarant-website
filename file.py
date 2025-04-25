'''
file_obj=open('first_txt','rt')
while True:
    line=input('enter line: ')
    file_obj.write(line)
    ch=input('y to continue and x to exit')
    if ch=='x':
        break
file_obj.close()
'''
'''
file_obj=open('first_txt','rt')
line = file_obj.read()
print(line)
file_obj.close()
'''
'''
file_obj=open('first.txt','rt')
print(file_obj.read(10))
print(file_obj.tell())
file_obj.close()
'''
file_obj=open('first.txt','rt')
size=len(file_obj.read())
print('size of the file: ',size,'bytes')
file_obj.close()

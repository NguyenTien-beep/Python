f= open('demofile.txt','r')
print(f.read())

f.close()


with open('demofile.txt', 'r') as q:
    print(q.read(5))
    
with open('demofile.txt','r') as e:
    print(e.readline())
    print(e.readline())

with open('demofile.txt','r') as f:
    for x in f:
        print(x)
    
#Write
with open('demofile.txt','a') as f:
    f.write('\n day la menu')

with open('demofile.txt') as f:
    print(f.read())
    f.close()


#create file

#del
import os
if os.path.exists('Myfile.txt'):
    os.remove('Myfile.txt')
    print('this file was removed')
else:
    print('this file not exits')

#rm fildor
os.rmdir('Folder')
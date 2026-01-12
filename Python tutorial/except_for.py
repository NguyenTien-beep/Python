# try:
#     print('hello')
# # except NameError:
# #     print('variable x is not defined')
# except:
#     print('something else went wrongt')
# 
# # else:
# #     print('nothing went wrong')
# finally:
#     print('the try except is finished')

try:
    f=open('demofile.txt')
    try:
        f.wrife('lorum ipsum')
    except:
        print('sommething went wrong when writing to the file')
    finally:
        f.close()
except:
    print('something went wrong when opening the file')
    
# x=-1
# if x<0:
#     raise Exception('sorry, no number below zezo')

x='hello'
if not type(x) is int:
    raise TypeError('Only integers are allowed')
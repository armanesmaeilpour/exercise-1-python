state=input('moadele khod ra vared koind: ')
for i in state:
    if i=='+' :
        x = state.split('+')
        print(int(x[0]) + int(x[1]))
    elif i=='-' :
         x = state.split('-')
         print(int(x[0]) - int(x[1]))
    elif i=='*' :
         x = state.split('*')
         print(int(x[0]) * int(x[1]))
    elif i=='/' :
         x = state.split('/')
         print(int(x[0]) / int(x[1]))
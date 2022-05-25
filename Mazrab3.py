varMazrab=input('yek adad vared konid: ')
if  varMazrab.isnumeric() :
    varMazrab=int(varMazrab)
    varMazrab=((varMazrab//10)+1)*10
    print('mazrab badi barabar ast ba: ', varMazrab)
else:
    print('moteghayer haye vared shode adad nistand')
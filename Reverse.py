var1=input('adad ra vared konid: ')
length=len(var1)
i=0
varList=[]
varOut= ''
if var1.isnumeric():
    while i < len(var1):
        varList.insert(i,var1[length-i-1])
        i += 1
    for j in varList:
        varOut += j
    print(varOut)
else:
    print('moteghayer vared shode adad nist')
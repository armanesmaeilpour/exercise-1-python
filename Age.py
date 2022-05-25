age=input('sen shoma cheghadr ast? ')
if age.isnumeric():
    age=int(age)
    if age > 40:
        print('pir kaftari hasti vase khodet')
    elif age < 40 and age > 20:
        print('javooni hanooz dahanet boo shir mide')
    else :
        print('kooochooolooo')
else:
    print('meghdar vared shode sahih nist')
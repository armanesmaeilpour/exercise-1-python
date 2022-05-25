length=input('tool ea vared kinid: ')
width=input('arz ra vared konid: ')
if length.isnumeric() and width.isnumeric() :
    length=int(length)
    width=int(width)
    area=length*width
    print('masahat barabar ast ba: ', area)
else:
    print('moteghayer haye vared shode adad nistand')
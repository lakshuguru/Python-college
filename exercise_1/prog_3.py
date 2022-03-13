l=int(input('length'))
b=int(input('breadth'))
h=int(input('height'))
p=(l+b+h)/2
a=(p*(p-l)*(p-b)*(p-h))**0.5
print('area of triangle: {0}'.format(a))
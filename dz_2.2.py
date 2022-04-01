weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
res = ''
weather.insert(1, '"')
weather.insert(3, '"')
weather.insert(5, '"')
weather.insert(7, '"')
weather.insert(12, '"')
weather.insert(14, '"')
#print(weather)
weather[2] = '05'
weather[13] = '+05'
#print(weather)
for i in weather:
    res += i
    res += ' '
print(res)

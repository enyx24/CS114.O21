price = [int(num) for num in input().split()]

instore = 0
online = 0

def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

for i in price:
    text = input().split()
    if 'higher' in text:
        index = text.index('higher')
        text = text[index-1: index+1]
    elif 'lower' in text:
        index = text.index('lower')
        text = text[index-1: index+1]
    else:
        instore += i
        online += i
        continue
    if is_float(text[0]):
        text[0] = text[0][: -1]
        perc = float(text[0])
    else:
        instore += i
        online += i
        continue
    #print(text)
    if text[1] == 'higher':
        instore += i*(100-perc)/100
        online += i
    else:
        instore += i
        online += i*(100-perc)/100
cih = int(input())
#print(instore, online)
if cih >= instore or cih >= online:
    print('true')
else:
    print('false')

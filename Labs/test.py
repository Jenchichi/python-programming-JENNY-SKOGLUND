frukter = []
frukter.append('Äpple')
frukter.append('Banan')
frukter.append('Mango') #frukter = ['Äpple', 'Banan', 'Mango']
print(f'frukter = {frukter}')

frukter.pop(0) #ta bort första elementet, 'Äpple'.
print('frukter = ' + str(frukter))
frukter.pop(-1) #ta bort sista elementet, 'Mango'.
print('frukter = ' + str(frukter))

frukter = ['Äpple', 'Banan', 'Mango']
testfrukt = frukter[0]
print(testfrukt[-1])

frukter1 = ["jordgubbe" , "vindruva", 'grape']
godfrukt = frukter1[2]
print (godfrukt[-1])
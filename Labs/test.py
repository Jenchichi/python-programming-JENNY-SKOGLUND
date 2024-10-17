frukter = []
frukter.append('Äpple')
frukter.append('Banan')
frukter.append('Mango') #frukter = ['Äpple', 'Banan', 'Mango']
print(f'frukter = {frukter}')

frukter.pop(0) #ta bort första elementet, 'Äpple'.
print('frukter = ' + str(frukter))
frukter.pop(-1) #ta bort sista elementet, 'Mango'.
print('frukter = ' + str(frukter))

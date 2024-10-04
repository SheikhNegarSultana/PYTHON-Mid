socialMedia = ['Twitter' , 'Instagram' , 'FaceBook' , 'Whatsapp' , 'Telegram' , 'Imo']
socialMedia.remove('Imo')
print(socialMedia)

socialMedia = ['Twitter' , 'Instagram' , 'FaceBook' , 'Whatsapp' , 'Telegram' , 'Imo']
socialMedia.pop(4)
print(socialMedia)

socialMedia = ['Twitter' , 'Instagram' , 'FaceBook' , 'Whatsapp' , 'Telegram' , 'Imo']
socialMedia.pop()
print(socialMedia)

# socialMedia.clear()
# print(socialMedia)

for x in range(len(socialMedia)) :
    print(socialMedia[x])

negar = lambda a : a*a
print(negar(9))


# List Are Mutable ; Index Niye Change Kora Jay
socialMedia = ['Twitter' , 'Instagram' , 'FaceBook' , 'Whatsapp' , 'Telegram' , 'Imo']
socialMedia[0] = 'X'
print("Mutable : " , socialMedia )

#  Range Use Kore Element Change ; 2 Ta Por Por Element
socialMedia[ 1 : 3] = ['Linkedin' , 'YouTube']
print('socialMedia[ 1 : 3] Changed With LinkedIn and YouTube ' ,socialMedia)


#  Range Use Kore Element Change ; Change the Third value by replacing it with two new values
socialMedia1 = ['Twitter' , 'Instagram' , 'FaceBook' , 'Whatsapp' , 'Telegram' , 'Imo']
socialMedia1[ 2 : 3 ] = ['Linkedin' , 'YouTube']
print('socialMedia1[2] Changed : ' , socialMedia1)


# Range Use Kore Element Change ; Change the second and third value by replacing it with one value
socialMedia2 = ['Twitter' , 'Instagram' , 'FaceBook' , 'Whatsapp' , 'Telegram' , 'Imo']
socialMedia2[ 4 : 6 ] = ['Linkedin' , 'YouTube' , 'Pinterest']
print(socialMedia2)



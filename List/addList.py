# Method 1 : arrayName.append() Method Use Kora ; Last E Element Add Kore
streetFood = [ 'Jhal Muri' , 'Achar' , 'Chotpoti' , 'Lebur Sorbot' ]
streetFood.append('Alur Chop')
streetFood.append(' ')
print(streetFood)

#Method 2 : arrayName.insert(index , The Element I Want To Add)
streetFood = [ 'Jhal Muri' , 'Achar' , 'Chotpoti' , 'Lebur Sorbot' ]
streetFood.insert(2 , 'Ice Cream')
print(streetFood)

# Method 3 : arrayName.extend(arrayName) 
streetFood = [ 'Jhal Muri' , 'Achar' , 'Chotpoti' , 'Lebur Sorbot' ]
healthyFood = ['Salad' , True]

streetFood.extend(healthyFood)

print(streetFood) #Jar Sathe Add Korsi

'''
The Power Of arrayName.extend(arrayName)
List er sathe add kore : Tuple , Dictionary , Set
'''
# Example 1 :
streetFood = [ 'Jhal Muri' , 'Achar' , 'Chotpoti' , 'Lebur Sorbot' ] #List
healthyFood = ('Salad' , True) #Tuple
streetFood.extend(healthyFood)
print(streetFood) 

# Example 2 :
streetFood = [ 'Jhal Muri' , 'Achar' , 'Chotpoti' , 'Lebur Sorbot' ] #List
healthyFood = ('Salad' , True) #Tuple
moreFood = {
    'Fruits' : 'Apple' ,
    'Vegetable' : 'Carrot'
}
streetFood.extend(healthyFood)
streetFood.extend(moreFood.values()) #Dictonary Values
print(streetFood) 




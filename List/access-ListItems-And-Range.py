# Create A List
create_list = [1, 2, 'Hi' , True , 1 , 6]
print(create_list)

''' 
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

1. Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the 'end of the list'.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

'''

# Allow Duplicates
duplicateValuedList = [1, 'Apple' , 2 , 1 , 'Cherry' , 4 ,' ']
print('duplicateValuedList : ' , duplicateValuedList )

# List Length using " len(List Name) "
print(len(duplicateValuedList))

# List Type using " type( List Name ) "
print(type(duplicateValuedList))

# List Constructor
listConstructor = list(('Hi' , 'Hello' , 'Bye' , 'Tata'))
print('listConstructor : ' , listConstructor )

# access List Item / List Iterable
print( duplicateValuedList[0])
print(duplicateValuedList[-2]) #Negative Indexing

#Range of Indexes
list_range = [ 9 , 89 , 78 , 90 , 89 , 97 , 77 , 88 ,99]
print( 'list_range[2:7] : ' , list_range[2:7] ) # Index : 2 Theke Suru Sesh 6 E

print('list_range[:7] :' , list_range[:7]) # Index : 0 Theke Suru Sesh 6 E

print('list_range[2:] : ' , list_range[2:]) # Index : 2 Theke Suru Sesh Last Porjonto

print('list_range[ : ] : ' , list_range[ : ]) # Shob Print Korbe

print('list_range[ -8 : -2 ] :' ,list_range[ -8 : -2 ] ) # Index : -8 Theke Suru Sesh -3 Porjonto ; 
# Note ----> Index : -1 = 99


#Check If Item Is In List Or Not
if 99 in list_range :
    print('99 is in the list')
else :
    print('Not Found')


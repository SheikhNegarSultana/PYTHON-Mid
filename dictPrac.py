person = {
    'name' : 'Negar',
    'age' : 25,
    'occupation' : {
        'job' : 'Software Engineer',
        'company' : 'Google'
        
    }
}

print(person['occupation']['company'])


def sum (a,b) :
    return a + b

sums = map(sum , (2,8) , (8,9))
print(sums)
print(list(sums))
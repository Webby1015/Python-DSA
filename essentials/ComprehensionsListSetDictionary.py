numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
# traditional method
for i in numbers:
    if i % 2 == 0:
        even.append(i)

# list comprehension
even = [i for i in numbers if i % 2 == 0]

# its a way to save lines

# another example

square = [i*i for i in numbers]
# it works exactly the same for sets but instead of [] we use {}
even = {i for i in numbers if i % 2 == 0}
# this code makes a of unique sequesnce of even numbers

#           zip function
cities = ["mumbai", "new york", "paris", "bla"]
countries = ["india", "usa", "france"]

z = zip(cities, countries)
print(z)  # z is a pointer of address
for a in z:
    print(a)  # a is a list having 2 elements one of each cities and countries
# any extra elements are ignored while zipping

#           Dictronary Comprehentions

d = {city: country for city, country in zip(cities, countries)}
print(d)

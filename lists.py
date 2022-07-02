lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","karen","jim","Oscar","toby"]
friends[3]="adcd"
friends.extend(lucky_numbers)
friends.append("nethan")
print(friends)
#tuples
coordinates = (4,5) #cannot be changed or modified
print(coordinates[1])

#tuples
(x, y) = (122, "abc")
print(y)
print(x)
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)
tupes = d.items()
print(tupes)
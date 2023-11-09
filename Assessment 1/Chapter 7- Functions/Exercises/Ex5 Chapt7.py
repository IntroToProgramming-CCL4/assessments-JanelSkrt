#This will print the countries and their capital cities.
def describe_city(city, country='UAE'):
    print (city,'is in the', country)
describe_city ('Beijing', 'China')
describe_city ('Abu Dhabi')
describe_city ('Costa Rica.', 'San Jose')
describe_city ('Dopenhagen', 'Denmark')
#This will print the city that is not in the default country.
describe_city ("Manila")
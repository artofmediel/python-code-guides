# dictionary comprehension = create dictionaries using an expression
#                          can replace for loops and certain lambda funcions
#
# dictionary = {key: expression for(key,value) in iterable}
# dictionary = {key: expression for(key,value) in iterable if conditional}
# dictionary = {key: (if/else) for(key,value) in iterable}
# dictionary = {key: function(value) for(key,value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# convert into celsius : (value-32)*(5/9) : round i to be readable
cities_in_C = {key: round((value-32)*(5/9)) for(key,value) in cities_in_F.items()}
print(cities_in_C)

# -------------------------
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# make a list where weather is sunny
sunny_weather = {key: value for(key,value) in weather.items() if value == "sunny"}
print(sunny_weather)

# -------------------------
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# describe weather temperatures : warm, cold, etc.
desc_cities = {key: ("warm" if value >= 40 else "cold") for (key,value) in cities.items()}
print(desc_cities)

# -------------------------
def check_temp(value):
    if value >=70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities_list = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# use a function to check temperature
check_temp_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(check_temp_cities)

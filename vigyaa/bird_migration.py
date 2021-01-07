""" You have been asked to help study the population of birds migrating across the continent.
 Each type of bird you are interested in will be identified by an integer value. 
 Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. 
 You would like to be able to find out which type of bird is most common given a list of sightings. 
 Your task is to print the type number of that bird and if two or more types of birds are equally common,
  choose the type with the smallest ID number. """

"""
solution to this is, 

step 1) we first convert the list into dictionary format and sort the dictionary.
step 2) we then find the max value in the dictionary. 
step 3) check weather there are any equal max values in the dictionary. 
step 4) if so then check the lowest key among them.

"""

from collections import Counter

list_values = [1, 2, 2, 3, 3]
    # [1, 2, 3, 4, 2, 1, 3, 1, 2, 3, 4, 1]


def bird_migration(lvalues):
    # convert the list into kv by using Counter function
    dictionary = Counter(lvalues)

    # get the highest value from the dict
    first_val = sorted(dictionary, key=dictionary.get, reverse=True)[0]

    # check if there are any similar highest values in dict
    similar_high_val = {}
    for k, v in dictionary.items():
        if v == dictionary[first_val]:
            similar_high_val[k] = v

    # finally return the min value if there are more similar highest values.
    return min(similar_high_val.keys())


print(bird_migration(list_values))

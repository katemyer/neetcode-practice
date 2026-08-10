from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    my_dict = {name: age}
    return my_dict
    


def list_to_dict(words: List[str]) -> Dict[str, int]:
    #create dictionary
    my_dict = {}

    #get the word at that position
    # range(len(words)) === range of how many are in the list
    # loop starting at i to loop through all the elements
    #useful bc need both index and value
    
    for i in range(len(words)):
    #store the word as the key ......assign it the value i
        my_dict[words[i]] = i
    #return the dic
    return my_dict




# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))

from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    result = []

    for key in age_dict:
        result.append(age_dict[key])
    return result

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))

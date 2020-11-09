from typing import Dict, List

returned_from_outside_func = 3.1

# dict where keys are strings and values are ints

name_counts: Dict[str, int] = {
    "Marc Benioff": 14,
    "Dave Wade-Stein": 6
}

# list of integers

val: int = 1
numbers: List[int] = [1, 2, 3, 4, 5, 6]

# list which holds dicts 
# each dict holds a string key / int value

list_of_dicts: List[Dict[str, int]] = [
    { "key1": 1, "key2": 2 },
    { "key": val,
      "something": returned_from_outside_func },
]

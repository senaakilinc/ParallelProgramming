def remove_duplicates(seq: list) -> list:
    return list(set(seq))

def list_counts(seq: list) -> dict:
    counts = {} 
    for item in seq:
      # If there is an item in the dictionary, increase its value by 1, otherwise start from 0 and add 1
        counts[item] = counts.get(item, 0) + 1
    return counts

def reverse_dict(d: dict) -> dict:
    reversed_dict = {} 
    for key, value in d.items():
        if value in reversed_dict:
            raise ValueError(f"Duplicate value found: {value}")
        reversed_dict[value] = key
    return reversed_dict

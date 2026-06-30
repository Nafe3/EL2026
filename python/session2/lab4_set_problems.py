"""Set Problems - Testing student capability with set operations."""


def set_operations(set1: set, set2: set) -> dict:
    """Perform basic set operations on two sets.

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        dict: Dictionary with union, intersection, difference, symmetric_difference
    """
    # Write your solution here
    return {"union":  set1.union(set2), "intersection":set1.intersection(set2), \
        "difference": set1.difference(set2), "symmetric_difference": set1.symmetric_difference(set2)}



def find_unique_elements(list1: list, list2: list) -> tuple:
    """Find elements that are unique to each list using sets.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        tuple: (unique_to_list1, unique_to_list2)
    """
    # Write your solution here
    set1 = set(list1)
    set2 = set(list2)
    return (set1.difference(set2),set2.difference(set1))


def remove_vowels_set(text):
    """Remove vowels from text using set operations.

    Args:
        text (str): Input text

    Returns:
        str: Text with vowels removed
    """
    # Write your solution here
    vowels = set("aeiouAEIOU")
    res = ""
    for char in text:
        if char not in vowels:
            res += char
    return res

def find_common_friends(friends: dict) -> set:
    """Find common friends between two friends lists.

    Args:
        friends (dict): Dictionary of friends and their friends

    Returns:
        set: Set of common friends
    """
    common_friends:set = set()
    friends_list = list(friends.values())   # Get all friends sets as a list

    for i in range(1, len(friends_list)):
        friend_set = friends_list[i]
        #print(f"Intersecting with set at index {i}: {friend_set}")  # i for zero-based index
        #print(type(friends_list[i-1].intersection(friend_set)))
        #print(friends_list[i-1].intersection(friend_set))
        common_friends.update(friends_list[i-1].intersection(friend_set))
    
        #print(f"Current intersection result: {common_friends}")
        
    #print("Common friends:", common_friends)
    return common_friends



if __name__ == "__main__":
    # Test cases
    print("Testing set_operations...")
    result = set_operations({1, 2, 3, 4}, {3, 4, 5, 6})
    assert result["union"] == {1, 2, 3, 4, 5, 6}, "Union test failed"
    assert result["intersection"] == {3, 4}, "Intersection test failed"
    assert result["difference"] == {1, 2}, "Difference test failed"
    assert result["symmetric_difference"] == {1, 2, 5, 6}, "Symmetric difference test failed"

    print("Testing find_unique_elements...")
    result = find_unique_elements([1, 2, 3, 4], [3, 4, 5, 6])
    assert result[0] == {1, 2}, f"Expected {{1, 2}}, got {result[0]}"
    assert result[1] == {5, 6}, f"Expected {{5, 6}}, got {result[1]}"

    print("Testing remove_vowels_set...")
    RESULT = remove_vowels_set("Hello World")
    assert "a" not in RESULT.lower(), "Vowels should be removed"
    assert "H" in RESULT and "l" in RESULT, "Consonants should remain"

    print("Testing find_common_friends...")
    friends = {
        "Alice": {"Bob", "Charlie", "David"},
        "Bob": {"Alice", "Charlie", "Eve"},
        "Charlie": {"Alice", "Bob", "Frank"},
    }
    result = find_common_friends(friends)
    assert result == {"Alice", "Charlie"}, "Common friends test failed"

    print("All tests passed!")

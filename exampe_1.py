# exaple 1: Write a function that receives a list as parameter and return how many elements it has; if it doesn't have any element return an error.

def count_elements(lst):
    if not lst:
        raise ValueError("The list is empty.")
    return len(lst)

print(count_elements([1, 2, 3]))  # Output: 3
print(count_elements([]))        # Raises ValueError: The list is empty.

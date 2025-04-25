
def char_count_dict(s: str, ignore_case: bool = False) -> dict:
    """
    Returns a dictionary with the count of each character in the string `s`.

    Parameters:
    - s (str): The input string.
    - ignore_case (bool): If True, count characters in a case-insensitive manner.

    Returns:
    - dict: A dictionary where keys are characters and values are their counts.
    """
    if ignore_case:
        s = s.lower()

    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1

    return count_dict





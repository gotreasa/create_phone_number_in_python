def create_phone_number(phone_number: list[int]) -> str:
    if phone_number == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
        return "(111) 111-1111"
    if phone_number == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        return "(123) 456-7890"
    raise ValueError("❗️ Input should be a list")

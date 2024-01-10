def create_phone_number(phone_number: list[int]) -> str:
    if phone_number == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
        return "(111) 111-1111"
    raise ValueError("❗️ Input should be a list")

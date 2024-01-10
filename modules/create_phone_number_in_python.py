def create_phone_number(phone_number: list[int]) -> str:
    if not isinstance(phone_number, list):
        raise ValueError("❗️ Input should be a list")
    if any(not isinstance(number, int) for number in phone_number):
        raise ValueError("❗️ Input should be a list of integers")
    if len(phone_number) != 10:
        raise ValueError("❗️ Input should be a list of 10 integers")
    return (
        f"({phone_number[0]}{phone_number[1]}{phone_number[2]})"
        f" {phone_number[3]}{phone_number[4]}{phone_number[5]}"
        f"-{phone_number[6]}{phone_number[7]}{phone_number[8]}{phone_number[9]}"
    )

import pytest
from modules import create_phone_number_in_python


def describe_create_phone_number():
    def should_error_when_not_list():
        """🧪 should give an error when something other than a list is passed"""
        with pytest.raises(ValueError, match="❗️ Input should be a list"):
            create_phone_number_in_python.create_phone_number("blah")

    def should_give_phone_number_for_1111111111():
        """🧪 should return (111) 111-1111 when the input is [1111111111]"""
        assert create_phone_number_in_python.create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"

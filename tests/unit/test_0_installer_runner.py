import pytest
from modules import create_phone_number_in_python


def describe_create_phone_number():
    def should_error_when_not_list():
        """🧪 should give an error when something other than a list is passed"""
        with pytest.raises(ValueError, match="❗️ Input should be a list"):
            create_phone_number_in_python.create_phone_number("blah")

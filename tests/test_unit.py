# tests/test_unit.py

def test_string_contains_expected_phrase():
    compliment = "You're doing great!"
    assert "great" in compliment

def test_compliment_capitalization():
    compliment = "you're awesome!"
    assert compliment.capitalize() == "You're awesome!"

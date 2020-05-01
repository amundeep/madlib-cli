from madlib_cli import __version__
from madlib_cli.madlib import parse_template
from madlib_cli.madlib import merge_with_user_input

def test_version():
    assert __version__ == '0.1.0'

def test_parse_template_string():
    test_string = "An {Adjective} is tested."
    parsed_contents, parsed_words = parse_template(test_string)
    expected_parsed_contents = "An {} is tested."
    expected_words = ("Adjective",)
    
    assert parsed_contents == expected_parsed_contents
    assert parsed_words == expected_words

def test_merge_with_user_input():
    parsed_contents = "An {} is tested."
    user_input = ["antelope"]
    expected_merge_string = "An antelope is tested."

    assert merge_with_user_input(parsed_contents, user_input) == expected_merge_string


from caseconvert import (
    split_words,
    to_camel,
    to_constant,
    to_kebab,
    to_pascal,
    to_snake,
    to_title,
)


def test_split_words_from_snake():
    assert split_words("snake_case") == ["snake", "case"]


def test_split_words_from_camel():
    assert split_words("camelCase") == ["camel", "Case"]


def test_split_words_from_pascal():
    assert split_words("PascalCase") == ["Pascal", "Case"]


def test_split_words_handles_acronyms():
    assert split_words("HTTPServer") == ["HTTP", "Server"]


def test_split_words_mixed_separators():
    assert split_words("Mixed_Case-String name") == ["Mixed", "Case", "String", "name"]


def test_to_snake():
    assert to_snake("PascalCase") == "pascal_case"
    assert to_snake("HTTPServer") == "http_server"
    assert to_snake("kebab-case") == "kebab_case"


def test_to_camel():
    assert to_camel("snake_case") == "snakeCase"
    assert to_camel("PascalCase") == "pascalCase"
    assert to_camel("kebab-case") == "kebabCase"


def test_to_pascal():
    assert to_pascal("snake_case") == "SnakeCase"
    assert to_pascal("http_server") == "HttpServer"


def test_to_kebab():
    assert to_kebab("PascalCase") == "pascal-case"
    assert to_kebab("snake_case") == "snake-case"


def test_to_constant():
    assert to_constant("camelCase") == "CAMEL_CASE"
    assert to_constant("snake_case") == "SNAKE_CASE"


def test_to_title():
    assert to_title("snake_case") == "Snake Case"


def test_empty_string():
    assert to_snake("") == ""
    assert to_camel("") == ""
    assert to_pascal("") == ""
    assert split_words("") == []


def test_single_word():
    assert to_snake("word") == "word"
    assert to_camel("word") == "word"
    assert to_pascal("word") == "Word"


def test_round_trip():
    original = "some_identifier_name"
    assert to_snake(to_pascal(original)) == original

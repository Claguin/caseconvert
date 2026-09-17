"""Case-conversion logic, implemented as pure, dependency-free functions.

The core idea: split any string into a list of words, then rejoin those words
with the separator and capitalization of the target convention.
"""

from __future__ import annotations

import re

#: "camelCase" -> "camel Case" (lowercase/digit followed by uppercase).
_CAMEL_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")
#: "HTTPServer" -> "HTTP Server" (acronym followed by a capitalized word).
_ACRONYM_BOUNDARY = re.compile(r"([A-Z]+)([A-Z][a-z])")
#: Any run of non-alphanumeric characters (underscores, hyphens, spaces, ...).
_NON_ALNUM = re.compile(r"[^A-Za-z0-9]+")


def split_words(text: str) -> list[str]:
    """Split ``text`` into words.

    Handles camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE,
    spaces, and acronyms such as ``HTTPServer``.
    """
    if not text:
        return []
    text = _CAMEL_BOUNDARY.sub(r"\1 \2", text)
    text = _ACRONYM_BOUNDARY.sub(r"\1 \2", text)
    text = _NON_ALNUM.sub(" ", text)
    return [word for word in text.split() if word]


def to_snake(text: str) -> str:
    """``PascalCase`` -> ``pascal_case``."""
    return "_".join(word.lower() for word in split_words(text))


def to_kebab(text: str) -> str:
    """``PascalCase`` -> ``pascal-case``."""
    return "-".join(word.lower() for word in split_words(text))


def to_camel(text: str) -> str:
    """``snake_case`` -> ``snakeCase`` (first word lowercased)."""
    words = split_words(text)
    if not words:
        return ""
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def to_pascal(text: str) -> str:
    """``snake_case`` -> ``SnakeCase``."""
    return "".join(word.capitalize() for word in split_words(text))


def to_constant(text: str) -> str:
    """``camelCase`` -> ``CAMEL_CASE``."""
    return "_".join(word.upper() for word in split_words(text))


def to_title(text: str) -> str:
    """``snake_case`` -> ``Snake Case``."""
    return " ".join(word.capitalize() for word in split_words(text))

"""caseconvert: convert strings between naming conventions."""

from .core import (
    split_words,
    to_camel,
    to_constant,
    to_kebab,
    to_pascal,
    to_snake,
    to_title,
)

__version__ = "0.1.0"

__all__ = [
    "split_words",
    "to_camel",
    "to_constant",
    "to_kebab",
    "to_pascal",
    "to_snake",
    "to_title",
]

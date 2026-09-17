# caseconvert

[![CI](https://github.com/Claguin/caseconvert/actions/workflows/ci.yml/badge.svg)](https://github.com/Claguin/caseconvert/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Convert strings between naming conventions — `snake_case`, `camelCase`,
`PascalCase`, `kebab-case`, `CONSTANT_CASE`, and `Title Case` — with a single
dependency-free library.

## Install

```console
pip install caseconvert
```

## Usage

```python
from caseconvert import to_snake, to_camel, to_pascal, to_kebab, to_constant

to_snake("PascalCase")      # "pascal_case"
to_camel("snake_case")      # "snakeCase"
to_pascal("http_server")    # "HttpServer"
to_kebab("PascalCase")      # "pascal-case"
to_constant("camelCase")    # "CAMEL_CASE"
```

It handles the hard cases, including acronyms and mixed separators:

```python
from caseconvert import to_snake, split_words

to_snake("HTTPServer")              # "http_server"
to_snake("Mixed_Case-String name")  # "mixed_case_string_name"
split_words("HTTPServer")           # ["HTTP", "Server"]
```

## API

| Function        | Example (`"PascalCase"`) |
| --------------- | ------------------------ |
| `to_snake`      | `pascal_case`            |
| `to_camel`      | `pascalCase`             |
| `to_pascal`     | `PascalCase`             |
| `to_kebab`      | `pascal-case`            |
| `to_constant`   | `PASCAL_CASE`            |
| `to_title`      | `Pascal Case`            |
| `split_words`   | `["Pascal", "Case"]`     |

## Design notes

- **One algorithm** — everything builds on `split_words`, which normalizes
  camelCase, PascalCase, snake_case, kebab-case, spaces, and acronyms into a
  plain word list; each `to_*` function is then a one-line rejoin.
- **Zero runtime dependencies** — stdlib `re` only, so it works anywhere.
- **Pure functions** — no state, no I/O, fully unit-testable.

## Development

```console
uv sync          # install dependencies
uv run pytest    # run the test suite
```

## Publishing to PyPI

```console
uv build
uv publish
```

---

MIT © David Frank

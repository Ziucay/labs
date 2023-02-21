# Framework
This projects uses FastAPI

### Advantages

- Fast to learn, good documentation, big community.

- Production-ready code.

- Automatic documentation.

- Fully compatible with the open standards for APIs.

You can find complete list on https://fastapi.tiangolo.com/.

### Disadvantages

- As all tied to FastAPI app, the main file
tend to crowd.

- It may have fewer study materials, than older frameworks, like Django
or Flask.

# Packages

## `pytz`

This library allows accurate and cross-platform timezone calculations. 

# Linter for code - flask8

## Usage

Type

   ```bash
   flake8 app_python/main.py
   ```

# Linter for docs - vale

## Usage

On the first usage and after `.vale.ini` change,
type

```bash
   vale sync
   ```

When you can check documents

   ```bash
   vale <path to document>
   ```

# Unit tests

For this project I created one test, which asserts that the
time returned in correct format. Due to simplicity of the code, I 
see no reason to check the timestamp itself, as we either use
the same commands we have in rest, or the check would be more
complicated than the rest itself(for example, by making request to
WorldTimeAPI).

## Best practices

I used `pytest` with `anyio` plugin for asynchoronous tests. `anyio`
supports both `asyncio` and `trio` libraries, and I chose `asyncio`,
as it is more popular. Warning: if we don't specify backend for
`anyio`, it would try to run both `trio` and `asyncio` backends, which
can break, if we don't have `trio` installed.

I found `pytest` better than `unittest` from standard library, as
it is more compact.

In writing tests I relied on [Python guide for writing tests](https://docs.python-guide.org/writing/tests/).
Also, I used [FastAPI documentation](https://fastapi.tiangolo.com/advanced/async-tests/).


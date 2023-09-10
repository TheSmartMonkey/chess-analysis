from models.hello_model import HttpMessageModel


def message() -> None:
    print("hello world !")


def inc(x: int) -> int:
    return x + 1


def http_message(message: str) -> HttpMessageModel:
    return HttpMessageModel(
        message=message,
        code=200,
    )

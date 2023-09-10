from src.functions.hello import http_message, inc, message


def main() -> None:
    message()
    value = inc(3)
    print(value)
    print(http_message("This is a test message").message)


if __name__ == "__main__":
    main()

from functions.hello import http_message, inc


def test_inc() -> None:
    # Given
    number = 3

    # When
    new_number = inc(3)

    # Then
    assert new_number == number + 1


def test_http_message() -> None:
    # Given
    message = "test message"

    # When
    response = http_message(message)

    # Then
    assert response.code == 200
    assert response.message == message

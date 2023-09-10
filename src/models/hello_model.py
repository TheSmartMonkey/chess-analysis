from dataclasses import dataclass


@dataclass
class HttpMessageModel:
    message: str
    code: int

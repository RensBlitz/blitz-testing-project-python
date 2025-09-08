class SmtpClient:
    def __init__(self, host: str, port: int) -> None:
        if host is None or host == "":
            raise ValueError("SMTP host must be provided")
        if port <= 0:
            raise ValueError("SMTP port must be positive")
        self._host = host
        self._port = port

    def send(self, to: str, subject: str, body: str) -> str:
        if to is None or to == "":
            raise ValueError("Recipient must be provided")
        if subject is None:
            raise ValueError("Subject cannot be null")
        if body is None:
            raise ValueError("Body cannot be null")
        return "msg-" + str(abs(hash(to + subject + body + self._host + str(self._port))))

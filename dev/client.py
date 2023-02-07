class Client:
    """Client for GitHub"""

    def __init__(
        self,
        name: str,
        login : str,
        password : str,
        balance : str
        ) -> None:
        self.name = name
        self.login = login
        self.password = password
        self.balance = balance
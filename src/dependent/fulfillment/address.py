class Address:
    def __init__(self, street: str, city: str, country: str) -> None:
        self._street = street
        self._city = city
        self._country = country

    @property
    def street(self) -> str:
        return self._street

    @property
    def city(self) -> str:
        return self._city

    @property
    def country(self) -> str:
        return self._country

    def __str__(self) -> str:
        return f"{self._street},{self._city},{self._country}"

class FulfillmentResult:
    def __init__(self, reservation_id: str, tracking_id: str) -> None:
        self._reservation_id = reservation_id
        self._tracking_id = tracking_id

    @property
    def reservation_id(self) -> str:
        return self._reservation_id

    @property
    def tracking_id(self) -> str:
        return self._tracking_id

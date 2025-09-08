from decimal import Decimal


class PaymentGatewayClient:
    def charge(self, amount: Decimal, currency: str, reference: str) -> str:
        if amount is None or amount <= Decimal("0"):
            raise ValueError("Amount must be positive")
        if currency is None or currency == "":
            raise ValueError("Currency must be provided")
        return "pay_" + str(abs(hash(f"{amount}{currency}{reference}")))

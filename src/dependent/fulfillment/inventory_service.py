class InventoryService:
    def reserve(self, product_id: str, quantity: int) -> str:
        if product_id is None or product_id == "":
            raise ValueError("productId must be provided")
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        return "res-" + str(abs(hash(product_id + str(quantity))))

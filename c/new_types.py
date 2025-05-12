from typing import Literal, TypedDict, Protocol, NewType, Optional, NotRequired
class CustomType:
    pass

custom = CustomType
# Использование Literal для ограничения возможных значений
OrderStatus = Literal[
    "pending",
    "confirmed",
    "shipped",
    "delivered",
    "canceled",
]
PaymentMethod = Literal["card", "cash", "crypto", "bank_transfer"]

# Создание алиасов для встроенных типов, когда имеет смысл добавить семантику
OrderId = NewType("OrderId", str)  # OrderId - это не просто строка, а именно ID заказа
Price = int # Цена в копейках (или другой валюте), без десятичных знаков
type Quantity = int  # python 3.12+

def example_function(
    order_id: OrderId,
    quantity: Quantity,
    price: Price,
) -> None:
    print(f"Order ID: {order_id}, Quantity: {quantity}")

example_function(OrderId("12345"), 2, 1000)

# Создание собственных типов с помощью TypedDict
class OrderItem(TypedDict):
    product_id: str
    name: str | None
    quantity: Quantity
    price: Price


class CustomerInfo(TypedDict):
    customer_id: str
    email: str
    shipping_address: str
    phone: str | None
    missing_field: NotRequired[str]

# Создание протоколов для структурной типизации
class PaymentProcessor(Protocol):
    def process(self, amount: Price, method: PaymentMethod) -> bool:
        ...


def process_order(
    order_id: OrderId,
    status: OrderStatus,
    payment_method: PaymentMethod,
    items: list[OrderItem],
    customer_info: CustomerInfo,
    payment_processor: Optional[PaymentProcessor] = None
) -> dict[str, object]:
    # Обработка заказа
    if status == "confirmed":
        # Подтверждение заказа
        pass
    elif status == "shipped":
        # Отправка заказа
        pass

    # Обработка оплаты
    if payment_processor and payment_method in ["card", "crypto"]:
        total_amount = sum(item["price"] * item["quantity"] for item in items)
        payment_processor.process(total_amount, payment_method)
    print(customer_info)

    return {"order_id": order_id, "status": status, "processed": True}

process_order(
    OrderId("12345"),
    "confirmed",
    "card",
    [
        OrderItem(**{"product_id": "p1", "name": "Product a", "quantity": 2, "price": 1000}),
        {"product_id": "p2", "name": "Product 2", "quantity": 1, "price": 2000}
    ],
    {
        "customer_id": "c1",
        "email": "123@gmail.com",
        "shipping_address": "123 Main St",
        "phone": "123 Main St",
        "missing_field": "123 Main St"
    },

)
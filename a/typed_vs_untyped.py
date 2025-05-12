def process_user_data(user_id, name, age, is_active, tags, metadata):
    user = {
        "id": user_id,
        "name": name,
        "age": age,
        "active": is_active,
        "tags": tags
    }

    if metadata:
        user.update(metadata)

    return user


from typing import Optional, Any


def process_user_data(
    user_id: int | str,
    name: str,
    age: int,
    is_active: bool,
    tags: list[str],
    metadata: Optional[dict[str, Any]] = None
) -> dict[str, Any]:
    user = {
        "id": user_id,
        "name": name,
        "age": age,
        "active": is_active,
        "tags": tags
    }

    if metadata:
        user.update(metadata)

    return user

process_user_data(
    user_id=123,
    name=123,
    age=30,
    is_active=True,
    tags=["admin", "user"],
)
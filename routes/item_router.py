from fastapi import APIRouter
from services.item import ItemService

item_router = APIRouter(prefix="/item")

item_service = ItemService()


@item_router.get("/all")
def get_items():
    return item_service.get_items()


@item_router.post("/add_to_cart")
def add_item_to_cart(item_id: int):
    return item_service.add_item_to_cart(item_id)


@item_router.post("/remove_from_cart")
def remove_from_cart(item_id: int):
    return item_service.remove_from_cart(item_id)

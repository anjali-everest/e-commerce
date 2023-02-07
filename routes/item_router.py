from fastapi import APIRouter
from services.item import ItemService

item_router = APIRouter(prefix="/item")

item_service = ItemService()

@item_router.get("/all")
def get_items():
    return item_service.get_items()

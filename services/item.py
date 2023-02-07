import json


class ItemService:
    def get_items(self):
        f = open('data.json')
        data = json.load(f)
        f.close()
        return data

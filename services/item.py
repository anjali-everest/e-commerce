import json


class ItemService:
    def get_items(self):
        f = open('data/data.json')
        data = json.load(f)
        f.close()
        return data

    def add_item_to_cart(self, item_id: int):
        f = open('data/data.json')
        data = json.load(f)
        f.close()
        for item in data:
            if item['id'] == item_id:
                item['addedToCart'] = True

        # Serializing json
        json_object = json.dumps(data, indent=4)

        # Writing back to file
        with open("data/data.json", "w") as outfile:
            outfile.write(json_object)
            outfile.close()

        return {"Added item to cart!"}

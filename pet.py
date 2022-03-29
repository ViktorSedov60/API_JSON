class Cat:

# with open('api_test.json', encoding='utf8') as f:
#         templates = json.load(f)

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def is_available(self):
        return True if self.quantity_in_stock > 0 else False

cat = [
    {
     "name": "Барон",
     "gender": "мальчик",
     "age": 2,
    },
    {
     "name": "Сэм",
     "gender": "мальчик",
     "age": 2,
    }]


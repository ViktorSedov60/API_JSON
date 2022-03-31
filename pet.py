class Cat:

# with open('api_test.json', encoding='utf8') as f:
#         templates = json.load(f)

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age



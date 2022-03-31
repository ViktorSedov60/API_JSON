from pet import Cat
c1 = Cat("Барон", "Мальчик", 2)
c2 = Cat("Cэм", "Мальчик", 2)

print("Имя:", c1.name,  "; Пол:", c1.gender,  "; Возраст(лет):", c1.age)
print("Имя:", c1.getName(),  "; Пол:", c1.getGender(),  "; Возраст(лет):", c1.getAge())
print("Имя:", c2.name,  "; Пол:", c2.gender,  "; Возраст(лет):", c2.age)
print("Имя:", c2.getName(),  "; Пол:", c2.getGender(),  "; Возраст(лет):", c2.getAge())

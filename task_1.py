# Завдання 1. Основний персонаж
class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"Ім'я: {self.name}, Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}")

    def attack_enemy(self, enemy):
        print(f"{self.name} атакує {enemy.name} на {self.attack} урону!")
        enemy.health -= self.attack
        if enemy.health < 0:
            enemy.health = 0
        print(f"{enemy.name} тепер має {enemy.health} здоров'я.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} відновив {amount} здоров'я. Зараз здоров'я: {self.health}")


# Завдання 3. Класи Героїв
class Warrior(Character):
    def __init__(self, name, level, health, attack, armor):
        super().__init__(name, level, health, attack)
        self.armor = armor

    def info(self):
        super().info()
        print(f"Броня: {self.armor}")

    def heal(self):
        super().heal(15)  # Воїн відновлює 15 здоров'я


class Mage(Character):
    def __init__(self, name, level, health, attack, mana):
        super().__init__(name, level, health, attack)
        self.mana = mana

    def info(self):
        super().info()
        print(f"Мана: {self.mana}")

    def heal(self):
        super().heal(20)  # Маг відновлює 20 здоров'я


class Archer(Character):
    def __init__(self, name, level, health, attack, arrows):
        super().__init__(name, level, health, attack)
        self.arrows = arrows

    def info(self):
        super().info()
        print(f"Стріли: {self.arrows}")

    def heal(self):
        super().heal(10)  # Лучник відновлює 10 здоров'я


# Демонстрація бою
if __name__ == "__main__":
    hero1 = Warrior("Борис", 5, 100, 20, armor=10)
    hero2 = Mage("Сергій", 5, 80, 25, mana=50)

    hero1.info()
    hero2.info()

    print("\n--- Початок бою ---")
    hero1.attack_enemy(hero2)
    hero2.attack_enemy(hero1)

    print("\n--- Відновлення здоров'я ---")
    hero1.heal()
    hero2.heal()

    print("\n--- Інформація після бою ---")
    hero1.info()
    hero2.info()

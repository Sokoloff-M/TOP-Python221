from typing import Optional


class Creature:
    """Обрабатываемый объект."""
    def __init__(self,
                 name: str,
                 default_attack: int,
                 default_defense: int):
        self.name = name.title()
        self.attack = default_attack
        self.defense = default_defense

    def __str__(self):
        return f'{self.name}: A={self.attack}, D={self.defense}'


class CreatureModifier:
    """Базовый класс для цепочки обработчиков. Запускает обработку данных."""
    def __init__(self, creature: Creature):
        # обрабатываемый объект
        self.creature = creature
        # поля для связи с другими обработчиками в цепочке
        self.previous_modifier: Optional['CreatureModifier'] = None
        self.next_modifier: Optional['CreatureModifier'] = None

    def add_modifier(self, modifier: 'CreatureModifier'):
        """Добавляет обработчик."""
        if self.next_modifier is None:
            self.next_modifier = modifier
            self.next_modifier.previous_modifier = self
        else:
            self.next_modifier.add_modifier(modifier)

    def handle(self):
        """Вызывает следующий обработчик в цепочке."""
        if self.next_modifier is not None:
            self.next_modifier.handle()

    def clear(self):
        if self.next_modifier is not None:
            self.next_modifier.clear()
        else:
            self.undo()

    def undo(self):
        self.next_modifier = None
        if self.previous_modifier is not None:
            self.previous_modifier.undo()
        self.previous_modifier = None


class DoubleAttackModifier(CreatureModifier):
    """Обработчик атаки."""
    def handle(self):
        """Модифицирует атрибуты обрабатываемого объекта."""
        self.creature.attack *= 2
        super().handle()

    def undo(self):
        self.creature.attack //= 2
        super().undo()


class IncreaseDefenseModifier(CreatureModifier):
    """Обработчик защиты."""
    def handle(self):
        """Модифицирует атрибуты обрабатываемого объекта."""
        if self.creature.attack <= 2*self.creature.defense:
            self.creature.defense += 1
        super().handle()

    def undo(self):
        """Модифицирует атрибуты обрабатываемого объекта."""
        if self.creature.attack <= 2*self.creature.defense:
            self.creature.defense -= 1
        super().undo()


goblin = Creature('Гоблин', 1, 1)
print(goblin)

inventory = CreatureModifier(goblin)

inventory.add_modifier(DoubleAttackModifier(goblin))
inventory.add_modifier(IncreaseDefenseModifier(goblin))
inventory.add_modifier(IncreaseDefenseModifier(goblin))

inventory.handle()
print(goblin)

inventory.clear()
print(goblin)
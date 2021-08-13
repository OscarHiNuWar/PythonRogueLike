from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item

class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        power_bonus: int = 0,
        defense_bonus: int = 0,
        range_limit: int = 0
    ):
        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus

'''Weapons'''
class Dagger(Equippable):
    def __init__(self, extra_power: int=0) -> None:
        super().__init__(
            equipment_type=EquipmentType.WEAPON, 
            power_bonus=2+extra_power, 
            )

class Spear(Equippable):
    def __init__(self, range: int = 0, extra_power: int=0) -> None:
        super().__init__(
            equipment_type=EquipmentType.WEAPON,
            range_limit = range,
            power_bonus=4+extra_power,
            )

class Sword(Equippable):
    def __init__(self, extra_power: int=0) -> None:
        super().__init__(
            equipment_type=EquipmentType.WEAPON, 
            power_bonus=4+extra_power)



'''Armors'''
class LeatherArmor(Equippable):
    def __init__(self, extra_power: int=0) -> None:
        super().__init__(
            equipment_type=EquipmentType.ARMOR, 
            defense_bonus=1+extra_power)


class ChainMail(Equippable):
    def __init__(self, extra_power: int=0) -> None:
        super().__init__(
            equipment_type=EquipmentType.ARMOR, 
            defense_bonus=3+extra_power)

    
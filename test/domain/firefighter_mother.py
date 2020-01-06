from typing import List

from fire_manager.domain.firefighter.firefighter import Firefighter


class FirefighterMother:

    @staticmethod
    def get_any_firefighter(
            firefighter_id="123",
            name="Tom",
            phone="+34666666666"
    ) -> Firefighter:
        return Firefighter(
            firefighter_id=firefighter_id,
            name=name,
            phone=phone
        )

    @staticmethod
    def get_any_list_of_firefighters(number_of_items=3) -> List[Firefighter]:
        firefighters_list = []
        for _ in range(0, number_of_items):
            firefighters_list.append(FirefighterMother.get_any_firefighter())
        return firefighters_list

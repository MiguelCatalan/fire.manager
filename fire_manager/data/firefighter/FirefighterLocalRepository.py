from typing import List

from interface import implements

from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.firefighter_repository import FirefighterRepository


class FirefighterLocalRepository(implements(FirefighterRepository)):

    def get_all_firefighters(self) -> List[Firefighter]:
        return [
            Firefighter(
                firefighter_id="123",
                email="tom@test.com",
                name="Tom",
                phone="+34666666666"
            ),
            Firefighter(
                firefighter_id="321",
                email="mot@test.com",
                name="Mot",
                phone="+34555555555"
            )
        ]

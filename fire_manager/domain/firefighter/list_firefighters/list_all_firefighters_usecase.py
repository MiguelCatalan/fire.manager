from typing import List

from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.firefighter_repository import FirefighterRepository


class ListAllFirefightersUseCase(object):

    def __init__(self, firefighters_repository: FirefighterRepository):
        self.firefighters_repository = firefighters_repository

    def execute(self) -> List[Firefighter]:
        firefighters = self.firefighters_repository.get_all_firefighters()
        return firefighters

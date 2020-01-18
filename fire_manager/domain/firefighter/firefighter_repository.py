from typing import List

from interface import Interface

from fire_manager.domain.firefighter.add_firefighter.new_firefighter_request import \
    NewFirefighterRequest
from fire_manager.domain.firefighter.firefighter import Firefighter


class FirefighterRepository(Interface):

    def get_all_firefighters(self) -> List[Firefighter]:
        pass

    def search_firefighter_by_email(self, email: str) -> Firefighter:
        pass

    def save_firefighter(self, request: NewFirefighterRequest) -> Firefighter:
        pass

    def get_firefighter(self, firefighter_id: str) -> Firefighter:
        pass

    def remove_firefighter(self, firefighter_id: str) -> bool:
        pass

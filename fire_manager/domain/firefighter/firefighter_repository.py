from typing import List

from interface import Interface

from fire_manager.domain.firefighter.firefighter import Firefighter


class FirefighterRepository(Interface):

    def get_all_firefighters(self) -> List[Firefighter]:
        pass

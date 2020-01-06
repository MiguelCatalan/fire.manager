import json
from typing import List

from fire_manager.domain.firefighter.firefighter import Firefighter


class FirefightersSerializers:

    @staticmethod
    def to_json(firefighters: List[Firefighter]) -> str:
        json_string = ', '.join(map(
            lambda firefighter: FirefighterSerializers.to_json(firefighter),
            firefighters
        ))
        return f"[{json_string}]"


class FirefighterSerializers:

    @staticmethod
    def to_json(firefighter: Firefighter) -> str:
        return json.dumps(firefighter.__dict__)

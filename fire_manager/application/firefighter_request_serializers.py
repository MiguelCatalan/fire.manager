import json

from fire_manager.domain.firefighter.add_firefighter.new_firefighter_request import \
    NewFirefighterRequest


class NewFirefighterRequestSerializers:

    @staticmethod
    def to_model(json_string: str) -> NewFirefighterRequest:
        new_firefighter_request_json = json.loads(json_string)
        return NewFirefighterRequest(
            new_firefighter_request_json.get("email", None),
            new_firefighter_request_json.get("name", None),
            new_firefighter_request_json.get("phone", None)
        )

import json


class RemoveFirefighterRequestSerializers:

    @staticmethod
    def to_model(json_string: str) -> str:
        remove_firefighter_request_json = json.loads(json_string)
        return remove_firefighter_request_json.get("id", "")

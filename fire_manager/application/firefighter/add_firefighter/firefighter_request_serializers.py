from fire_manager.domain.firefighter.add_firefighter.new_firefighter_request import \
    NewFirefighterRequest


class NewFirefighterRequestSerializers:

    @staticmethod
    def to_model(json_string) -> NewFirefighterRequest:
        return NewFirefighterRequest(
            json_string.get("email", None),
            json_string.get("name", None),
            json_string.get("phone", None)
        )

from fire_manager.domain.firefighter.add_firefighter.new_firefighter_request import \
    NewFirefighterRequest


class RequestNewFirefighterMother:

    @staticmethod
    def get_any_firefighter_request(
            email="test@smart.me",
            name="Tom",
            phone="+34666666666"
    ) -> NewFirefighterRequest:
        return NewFirefighterRequest(
            email=email,
            name=name,
            phone=phone
        )

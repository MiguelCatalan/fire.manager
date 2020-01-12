from fire_manager.application.firefighter_serializers import FirefighterSerializers
from fire_manager.application.firefighter_serializers import FirefightersSerializers
from test.domain.firefighter_mother import FirefighterMother

JSON_FIREFIGHTER = '{"firefighter_id": "123", "email": "test@smart.me", "name": "Tom", "phone": "+34666666666"}'
JSON_FIREFIGHTER_LIST = f'[{JSON_FIREFIGHTER}, {JSON_FIREFIGHTER}, {JSON_FIREFIGHTER}]'


class TestFirefighterSerializers:

    def test_should_serialize_firefighter_to_json(self):
        firefighter = FirefighterMother.get_any_firefighter()

        json_string = FirefighterSerializers.to_json(firefighter)

        assert json_string == JSON_FIREFIGHTER

    def test_should_serialize_firefighter_list_to_json(self):
        number_of_firefighter_in_list = 3
        firefighter_list = FirefighterMother.get_any_list_of_firefighters(
            number_of_firefighter_in_list)

        json_string = FirefightersSerializers.to_json(firefighter_list)

        assert json_string == JSON_FIREFIGHTER_LIST

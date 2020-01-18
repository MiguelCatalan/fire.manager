import json

from fire_manager.application.firefighter.remove_firefighter.remove_firefighter_request_serializers import \
    RemoveFirefighterRequestSerializers


class TestRemoveFirefighterRequestSerializers:

    def test_should_return_empty_string_if_id_not_present(self):
        json_request = json.loads("{}")

        subject = RemoveFirefighterRequestSerializers.to_model(json_request)

        assert subject == ""

    def test_should_return_the_id_as_string_if_id_is_present_in_the_body(self):
        json_request = json.loads('{"id": "1234"}')

        subject = RemoveFirefighterRequestSerializers.to_model(json_request)

        assert subject == "1234"

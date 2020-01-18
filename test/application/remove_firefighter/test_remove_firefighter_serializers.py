from fire_manager.application.firefighter.remove_firefighter.remove_firefighter_serializers import \
    RemoveFirefighterSerializers


class TestRemoveFirefighterSerializers:
    def test_should_return_successful_response(self):
        subject = RemoveFirefighterSerializers.to_json()

        assert subject == '{"message": "Firefighter successfully removed"}'

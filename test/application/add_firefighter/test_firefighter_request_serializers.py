from fire_manager.application.firefighter.add_firefighter.firefighter_request_serializers import \
    NewFirefighterRequestSerializers


class TestNewFirefighterRequestSerializers:
    def test_should_return_a_model_with_name_as_none_if_not_present(self):
        json_request = "{}"

        subject = NewFirefighterRequestSerializers.to_model(json_request)

        assert subject.name is None

    def test_should_return_a_model_with_email_as_none_if_not_present(self):
        json_request = "{}"

        subject = NewFirefighterRequestSerializers.to_model(json_request)

        assert subject.email is None

    def test_should_return_a_model_with_phone_as_none_if_not_present(self):
        json_request = "{}"

        subject = NewFirefighterRequestSerializers.to_model(json_request)

        assert subject.phone is None

    def test_should_return_a_model_with_name_if_present(self):
        json_request = '{"name": "TOM"}'

        subject = NewFirefighterRequestSerializers.to_model(json_request)

        assert subject.name == "TOM"

    def test_should_return_a_model_with_email_if_present(self):
        json_request = '{"email": "tom@sm.com"}'

        subject = NewFirefighterRequestSerializers.to_model(json_request)

        assert subject.email == "tom@sm.com"

    def test_should_return_a_model_with_phone_if_present(self):
        json_request = '{"phone": "+34666666666"}'

        subject = NewFirefighterRequestSerializers.to_model(json_request)

        assert subject.phone == "+34666666666"

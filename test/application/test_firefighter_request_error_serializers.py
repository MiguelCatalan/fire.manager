import pytest
from chalice import ConflictError, UnprocessableEntityError, ChaliceViewError

from fire_manager.application.firefighter_request_error_serializers import \
    NewFirefighterErrorSerializers
from fire_manager.domain.firefighter.add_firefighter.add_firefighter_usecase import \
    FirefighterAlreadyRegistered, MissingMandatoryFields


class TestNewFirefighterErrorSerializers:

    def test_should_return_a_409_http_error_if_firefighter_already_exists(self):
        exception = FirefighterAlreadyRegistered()

        with pytest.raises(ConflictError) as exception_raised:
            NewFirefighterErrorSerializers.to_http_error(exception)

        assert exception_raised.value.STATUS_CODE == 409
        assert str(
            exception_raised.value) == "ConflictError: Firefighter already exists, can't add it again"

    def test_should_return_a_422_http_error_if_any_parameter_is_missing(self):
        exception = MissingMandatoryFields(MissingMandatoryFields.NAME_IS_MISSING)

        with pytest.raises(UnprocessableEntityError) as exception_raised:
            NewFirefighterErrorSerializers.to_http_error(exception)

        assert exception_raised.value.STATUS_CODE == 422
        assert str(
            exception_raised.value) == 'UnprocessableEntityError: Necessary arguments missing: Field "name" is mandatory'

    def test_should_return_a_500_http_error_if_any_other_error_is_raised(self):
        exception = StopIteration()

        with pytest.raises(ChaliceViewError) as exception_raised:
            NewFirefighterErrorSerializers.to_http_error(exception)

        assert exception_raised.value.STATUS_CODE == 500
        assert str(
            exception_raised.value) == 'ChaliceViewError: An unknown error had happen ¯\_(ツ)_/¯'

import pytest
from chalice import UnprocessableEntityError, ChaliceViewError, NotFoundError

from fire_manager.application.firefighter.remove_firefighter.remove_firefighter_error_serializers import \
    RemoveFirefighterErrorSerializers
from fire_manager.domain.firefighter.remove_firefighter.remove_firefighter_usecase import \
    MissingMandatoryId, FirefighterNotFound, CouldNotRemoveFirefighter


class TestRemoveFirefighterErrorSerializers:

    def test_should_return_a_404_http_error_if_firefighter_does_not_exists(self):
        exception = FirefighterNotFound()

        with pytest.raises(NotFoundError) as exception_raised:
            RemoveFirefighterErrorSerializers.to_http_error(exception)

        assert exception_raised.value.STATUS_CODE == 404
        assert str(
            exception_raised.value) == "NotFoundError: Firefighter does not exists"

    def test_should_return_a_422_http_error_if_any_parameter_is_missing(self):
        exception = MissingMandatoryId(MissingMandatoryId.ID_IS_MISSING)

        with pytest.raises(UnprocessableEntityError) as exception_raised:
            RemoveFirefighterErrorSerializers.to_http_error(exception)

        assert exception_raised.value.STATUS_CODE == 422
        assert str(
            exception_raised.value) == 'UnprocessableEntityError: Necessary arguments missing: Field "id" is mandatory'

    def test_should_return_a_500_http_error_if_the_request_fails(self):
        exception = CouldNotRemoveFirefighter()

        with pytest.raises(ChaliceViewError) as exception_raised:
            RemoveFirefighterErrorSerializers.to_http_error(exception)

        assert exception_raised.value.STATUS_CODE == 500
        assert str(
            exception_raised.value) == "ChaliceViewError: Could not remove the firefighter"

    def test_should_return_a_500_http_error_if_any_other_error_is_raised(self):
        exception = StopIteration()

        with pytest.raises(ChaliceViewError) as exception_raised:
            RemoveFirefighterErrorSerializers.to_http_error(exception)

        assert exception_raised.value.STATUS_CODE == 500
        assert str(
            exception_raised.value) == 'ChaliceViewError: An unknown error had happen ¯\_(ツ)_/¯'

import pytest
from unittest.mock import Mock

from fire_manager.domain.firefighter.add_firefighter.add_firefighter_usecase import \
    AddFirefighterUseCase, MissingMandatoryFields, FirefighterAlreadyRegistered
from fire_manager.domain.firefighter.add_firefighter.new_firefighter_request import \
    NewFirefighterRequest
from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.firefighter_repository import FirefighterRepository
from test.domain.add_firefighter.request_new_firefighter_mother import RequestNewFirefighterMother
from test.domain.firefighter_mother import FirefighterMother


class TestAddFirefighterUseCase:

    def test_should_raise_missing_mandatory_fields_if_request_has_email_field_empty(self):
        request: NewFirefighterRequest = RequestNewFirefighterMother.get_any_firefighter_request(
            email=None)
        repository: FirefighterRepository = Mock()
        subject = AddFirefighterUseCase(repository)

        with pytest.raises(MissingMandatoryFields) as exception:
            subject.execute(request)

        assert str(exception.value) == MissingMandatoryFields.EMAIL_IS_MISSING

    def test_should_raise_missing_mandatory_fields_if_request_has_name_field_empty(self):
        request: NewFirefighterRequest = RequestNewFirefighterMother.get_any_firefighter_request(
            name=None)
        repository: FirefighterRepository = Mock()
        subject = AddFirefighterUseCase(repository)

        with pytest.raises(MissingMandatoryFields) as exception:
            subject.execute(request)

        assert str(exception.value) == MissingMandatoryFields.NAME_IS_MISSING

    def test_should_raise_missing_mandatory_fields_if_request_has_phone_field_empty(self):
        request: NewFirefighterRequest = RequestNewFirefighterMother.get_any_firefighter_request(
            phone=None)
        repository: FirefighterRepository = Mock()
        subject = AddFirefighterUseCase(repository)

        with pytest.raises(MissingMandatoryFields) as exception:
            subject.execute(request)

        assert str(exception.value) == MissingMandatoryFields.PHONE_IS_MISSING

    def test_should_raise_firefighter_already_registered_if_request_has_phone_field_empty(self):
        request: NewFirefighterRequest = RequestNewFirefighterMother.get_any_firefighter_request()
        repository: FirefighterRepository = Mock()

        repository.search_firefighter_by_email.return_value = \
            FirefighterMother.get_any_firefighter()
        subject = AddFirefighterUseCase(repository)

        with pytest.raises(FirefighterAlreadyRegistered):
            subject.execute(request)

    def test_should_request_saving_firefighter_if_request_is_valid(self):
        request: NewFirefighterRequest = RequestNewFirefighterMother.get_any_firefighter_request()
        repository: FirefighterRepository = Mock()

        repository.search_firefighter_by_email.return_value = None
        subject = AddFirefighterUseCase(repository)
        subject.execute(request)

        repository.save_firefighter.assert_called_once_with(request)

    def test_should_firefighter_if_request_is_valid(self):
        request: NewFirefighterRequest = RequestNewFirefighterMother.get_any_firefighter_request()
        repository: FirefighterRepository = Mock()

        repository.search_firefighter_by_email.return_value = None
        repository.save_firefighter.return_value = FirefighterMother.get_any_firefighter(
            name=request.name,
            email=request.email,
            phone=request.phone
        )
        subject = AddFirefighterUseCase(repository)
        firefighter: Firefighter = subject.execute(request)

        assert_firefighter_is_same_as_request(firefighter, request)


def assert_firefighter_is_same_as_request(firefighter: Firefighter, request: NewFirefighterRequest):
    assert firefighter.email == request.email
    assert firefighter.name == request.name
    assert firefighter.phone == request.phone

from unittest.mock import Mock

import pytest

from fire_manager.domain.firefighter.firefighter_repository import FirefighterRepository
from fire_manager.domain.firefighter.remove_firefighter.remove_firefighter_usecase import \
    RemoveFirefighterUseCase, MissingMandatoryId, FirefighterNotFound, CouldNotRemoveFirefighter
from test.domain.firefighter_mother import FirefighterMother


class TestRemoveFirefighterUseCase:

    def test_should_return_missing_mandatory_id_exception_if_id_is_missing(self):
        firefighter_repository: FirefighterRepository = Mock()
        subject: RemoveFirefighterUseCase = RemoveFirefighterUseCase(firefighter_repository)

        with pytest.raises(MissingMandatoryId):
            subject.execute("")

    def test_should_return_missing_mandatory_id_exception_if_id_is_an_space(self):
        firefighter_repository: FirefighterRepository = Mock()
        subject: RemoveFirefighterUseCase = RemoveFirefighterUseCase(firefighter_repository)

        with pytest.raises(MissingMandatoryId):
            subject.execute(" ")

    def test_should_return_firefighter_not_found_exception_if_id_is_wrong(self):
        firefighter_repository: FirefighterRepository = Mock()

        firefighter_repository.get_firefighter.return_value = None
        subject: RemoveFirefighterUseCase = RemoveFirefighterUseCase(firefighter_repository)

        with pytest.raises(FirefighterNotFound):
            subject.execute("1234")

    def test_should_return_could_not_remove_firefighter_if_can_remove_it(self):
        firefighter_repository: FirefighterRepository = Mock()

        firefighter_repository.get_firefighter.return_value = FirefighterMother.get_any_firefighter()
        firefighter_repository.remove_firefighter.return_value = False
        subject: RemoveFirefighterUseCase = RemoveFirefighterUseCase(firefighter_repository)

        with pytest.raises(CouldNotRemoveFirefighter):
            subject.execute("1234")

    def test_should_return_true_if_firefighter_is_removed(self):
        firefighter_repository: FirefighterRepository = Mock()
        firefighter_repository.get_firefighter.return_value = FirefighterMother.get_any_firefighter()
        firefighter_repository.remove_firefighter.return_value = True
        subject: RemoveFirefighterUseCase = RemoveFirefighterUseCase(firefighter_repository)

        has_been_removed = subject.execute("1234")

        assert has_been_removed is True

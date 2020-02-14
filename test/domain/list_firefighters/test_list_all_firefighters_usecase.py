from typing import List
from unittest.mock import Mock

from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.firefighter_repository import FirefighterRepository
from fire_manager.domain.firefighter.list_firefighters.list_all_firefighters_usecase import \
    ListAllFirefightersUseCase
from test.domain.firefighter_mother import FirefighterMother


class TestListAllFirefightersUseCase:

    def test_should_return_empty_if_there_is_no_firefighter(self):
        repository: FirefighterRepository = Mock()
        subject = ListAllFirefightersUseCase(repository)
        repository.get_all_firefighters.return_value = list()

        firefighter_list: List[Firefighter] = subject.execute()

        assert len(firefighter_list) == 0

    def test_should_return_list(self):
        repository: FirefighterRepository = Mock()
        subject = ListAllFirefightersUseCase(repository)
        repository.get_all_firefighters.return_value = \
            FirefighterMother.get_any_list_of_firefighters(number_of_items=2)

        firefighter_list: List[Firefighter] = subject.execute()

        assert len(firefighter_list) == 2

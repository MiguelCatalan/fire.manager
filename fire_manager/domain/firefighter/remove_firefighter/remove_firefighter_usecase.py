from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.firefighter_repository import FirefighterRepository


class MissingMandatoryId(Exception):
    ID_IS_MISSING = 'Field "id" is mandatory'


class FirefighterNotFound(Exception):
    pass


class CouldNotRemoveFirefighter(Exception):
    pass


class RemoveFirefighterUseCase(object):

    def __init__(self, firefighter_repository: FirefighterRepository):
        self.firefighter_repository = firefighter_repository

    def execute(self, firefighter_id: str) -> bool:
        normalized_firefighter_id = firefighter_id.strip()

        self.__validate_id(normalized_firefighter_id)
        self.__check_if_firefighter_exists(normalized_firefighter_id)
        self.__remove_firefighter(normalized_firefighter_id)
        return True

    def __validate_id(self, firefighter_id):
        if firefighter_id == "":
            raise MissingMandatoryId(MissingMandatoryId.ID_IS_MISSING)

    def __check_if_firefighter_exists(self, firefighter_id):
        firefighter: Firefighter = self.firefighter_repository.get_firefighter(firefighter_id)
        if firefighter is None:
            raise FirefighterNotFound()

    def __remove_firefighter(self, firefighter_id):
        has_been_removed: bool = self.firefighter_repository.remove_firefighter(firefighter_id)
        if not has_been_removed:
            raise CouldNotRemoveFirefighter()

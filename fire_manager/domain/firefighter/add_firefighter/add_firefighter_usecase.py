from fire_manager.domain.firefighter.add_firefighter.new_firefighter_request import \
    NewFirefighterRequest
from fire_manager.domain.firefighter.firefighter import Firefighter
from fire_manager.domain.firefighter.firefighter_repository import FirefighterRepository


class MissingMandatoryFields(Exception):
    EMAIL_IS_MISSING = 'Field "email" is mandatory'
    NAME_IS_MISSING = 'Field "name" is mandatory'
    PHONE_IS_MISSING = 'Field "phone" is mandatory'
    pass


class FirefighterAlreadyRegistered(Exception):
    pass


class AddFirefighterUseCase(object):

    def __init__(self, firefighter_repository: FirefighterRepository):
        self.firefighter_repository = firefighter_repository

    def execute(self, new_firefighter_request: NewFirefighterRequest) -> Firefighter:
        self.__validate_fields(new_firefighter_request)
        self.__validate_firefighter_is_not_already_added(new_firefighter_request)

        firefighter: Firefighter = self.firefighter_repository.save_firefighter(
            new_firefighter_request)

        return firefighter

    def __validate_fields(self, new_firefighter_request: NewFirefighterRequest):
        if new_firefighter_request.email is None:
            raise MissingMandatoryFields(MissingMandatoryFields.EMAIL_IS_MISSING)
        elif new_firefighter_request.name is None:
            raise MissingMandatoryFields(MissingMandatoryFields.NAME_IS_MISSING)
        elif new_firefighter_request.phone is None:
            raise MissingMandatoryFields(MissingMandatoryFields.PHONE_IS_MISSING)

    def __validate_firefighter_is_not_already_added(
            self,
            new_firefighter_request: NewFirefighterRequest
    ):
        already_added_firefighter = \
            self.firefighter_repository.search_firefighter_by_email(new_firefighter_request.email)

        if already_added_firefighter is not None:
            raise FirefighterAlreadyRegistered()

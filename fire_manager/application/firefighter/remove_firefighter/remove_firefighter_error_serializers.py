from chalice import ChaliceViewError, UnprocessableEntityError, NotFoundError

from fire_manager.domain.firefighter.remove_firefighter.remove_firefighter_usecase import \
    MissingMandatoryId, FirefighterNotFound, CouldNotRemoveFirefighter


class RemoveFirefighterErrorSerializers:
    UNKNOWN_ERROR = "An unknown error had happen ¯\_(ツ)_/¯"
    MISSING_MANDATORY_FIELDS_MESSAGE = "Necessary arguments missing: "
    FIREFIGHTER_NOT_FOUND_MESSAGE = "Firefighter does not exists"
    FIREFIGHTER_REMOVE_ERROR_MESSAGE = "Could not remove the firefighter"

    @staticmethod
    def to_http_error(domain_exception: Exception):
        if domain_exception.__class__ is MissingMandatoryId:
            raise UnprocessableEntityError(
                RemoveFirefighterErrorSerializers.MISSING_MANDATORY_FIELDS_MESSAGE + str(
                    domain_exception))
        elif domain_exception.__class__ is FirefighterNotFound:
            raise NotFoundError(RemoveFirefighterErrorSerializers.FIREFIGHTER_NOT_FOUND_MESSAGE)
        elif domain_exception.__class__ is CouldNotRemoveFirefighter:
            raise ChaliceViewError(
                RemoveFirefighterErrorSerializers.FIREFIGHTER_REMOVE_ERROR_MESSAGE)
        else:
            raise ChaliceViewError(RemoveFirefighterErrorSerializers.UNKNOWN_ERROR)

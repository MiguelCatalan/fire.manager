from chalice import ConflictError, ChaliceViewError, UnprocessableEntityError

from fire_manager.domain.firefighter.add_firefighter.add_firefighter_usecase import \
    FirefighterAlreadyRegistered, MissingMandatoryFields


class NewFirefighterErrorSerializers:
    UNKNOWN_ERROR = "An unknown error had happen ¯\_(ツ)_/¯"
    FIREFIGHTER_ALREADY_REGISTERED_MESSAGE = "Firefighter already exists, can't add it again"
    MISSING_MANDATORY_FIELDS_MESSAGE = "Necessary arguments missing: "

    @staticmethod
    def to_http_error(domain_exception: Exception):
        if domain_exception.__class__ is FirefighterAlreadyRegistered:
            raise ConflictError(
                NewFirefighterErrorSerializers.FIREFIGHTER_ALREADY_REGISTERED_MESSAGE)
        elif domain_exception.__class__ is MissingMandatoryFields:
            raise UnprocessableEntityError(
                NewFirefighterErrorSerializers.MISSING_MANDATORY_FIELDS_MESSAGE + str(
                    domain_exception))
        else:
            raise ChaliceViewError(NewFirefighterErrorSerializers.UNKNOWN_ERROR)

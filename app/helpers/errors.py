class LegacyMethodNotFound(Exception):
    """Raise when not found method in legacy"""

    pass


class UPermissionDenied(Exception):
    pass


class UForbidden(Exception):
    pass


class AliTokenInvalid(Exception):
    pass


class UNotFound(Exception):
    """Raise when not found upinus resource"""

    pass


class UUnprocessableEntity(Exception):
    pass


class UConflict(Exception):
    pass


class AliConnectFailure(Exception):
    pass


class UKafkaProduceError(Exception):
    pass


class UBadRequest(Exception):
    pass


class URateLimit(Exception):
    pass


class InvalidParamerters(Exception):
    pass


class OtherPaymentProcessing(Exception):
    pass


class OrderPaidError(Exception):
    pass


class UTimeoutError(Exception):
    pass

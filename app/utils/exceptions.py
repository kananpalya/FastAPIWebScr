from fastapi import HTTPException

class NotFoundException(HTTPException):
    """
    Exception raised when a requested resource is not found (HTTP 404).
    
    Args:
        detail (str): Optional detail message. Defaults to "Not found".
    """
    def __init__(self, detail: str = "Not found"):
        super().__init__(status_code=404, detail=detail)

class BadRequestException(HTTPException):
    """
    Exception raised when a bad request is made by the client (HTTP 400).
    
    Args:
        detail (str): Optional detail message. Defaults to "Bad request".
    """
    def __init__(self, detail: str = "Bad request"):
        super().__init__(status_code=400, detail=detail)

class UnauthorizedException(HTTPException):
    """
    Exception raised when authentication fails or is missing (HTTP 401).
    
    Args:
        detail (str): Optional detail message. Defaults to "Unauthorized".
    """
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(status_code=401, detail=detail)

class ForbiddenException(HTTPException):
    """
    Exception raised when the client does not have permission to access a resource (HTTP 403).
    
    Args:
        detail (str): Optional detail message. Defaults to "Forbidden".
    """
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(status_code=403, detail=detail)

class ConflictException(HTTPException):
    """
    Exception raised when there is a conflict with the current state of the resource (HTTP 409).
    
    Args:
        detail (str): Optional detail message. Defaults to "Conflict".
    """
    def __init__(self, detail: str = "Conflict"):
        super().__init__(status_code=409, detail=detail)

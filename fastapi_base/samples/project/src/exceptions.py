"""
Define your global custom exceptions in this file
"""

from fastapi import HTTPException, status


class BadRequestException(HTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail  = "Bad Request to"


class NotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "The requested resource was not found"


class UnauthorizedException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "You are not authorized to access this resource"

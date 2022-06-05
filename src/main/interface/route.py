from abc import ABC, abstractclassmethod
from typing import Type

from src.presenters.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """interface to routes"""

    @abstractclassmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """defining route"""

        raise Exception("should implement method: route")

from typing import Dict


class HttpRequest:
    """class to http_request representation"""

    def __init__(self, header: Dict = None, body: Dict = None, query: Dict = None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self):
        return (
            "HttpRequest (header={self.header}, body={self.body}, query={self.query})"
        )


class HttpResponse:
    """class to http_response representation"""

    def __init__(self, status_code: Dict = None, body: Dict = None):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return "HttpRequest (status_code={self.status_code}, body={self.body})"

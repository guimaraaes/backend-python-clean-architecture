class HttpErrors:
    """class to define errors in http"""

    @staticmethod
    def error_422():
        """HTTP 422"""
        return {"status_code": 422, "body": {"error": "unprocessable entirty"}}

    @staticmethod
    def error_400():
        """HTTP 400"""
        return {"status_code": 400, "body": {"error": "bag request"}}

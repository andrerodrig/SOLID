""" Dependency Inversion Principle """

"""
High and Low levels abstractions should depend on abstractions,
not High level depending on Low level.
"""

# Implementação errada

class XMLHttpService(XMLHttpRequestService):
    pass


class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service

    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.xml_http_service.request(url, 'POST')

#-----------------------------------

# Implementação correta

class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError


class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection

    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')


class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options: dict):
        self.xhr.open()
        self.xhr.send()


class NodeHttpService(Connection):
    def request(self, url: str, options: dict):
        pass


class MockHttpService(Connection):
    def request(self, url: str, options: dict):
        pass

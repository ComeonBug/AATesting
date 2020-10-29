from AATestingApi.basic_api import BasicApi


class ApiHttpbinGet(BasicApi):
    url = "https://httpbin.org/get"
    method = "GET"


class ApiHttpbinPost(BasicApi):
    url = "https://httpbin.org/post"
    method = "POST"
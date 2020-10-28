import json
from AATestingApi.basic_api import BasicApi


class ApiHttpbinGet(BasicApi):
    url = "https://httpbin.org/get"
    method = "GET"


class ApiHttpbinPost(BasicApi):
    url = "https://httpbin.org/post"
    method = "POST"


class TestCore:

    def test_get(self):
        ApiHttpbinGet().run().validate('status_code', 200)

    def test_get_params(self):
        ApiHttpbinGet().set_params(abc=123, xyz=345).run().validate('url', 'https://httpbin.org/get?abc=123&xyz=345')

    def test_post_json(self):
        request_body = {"a": "1"}
        ApiHttpbinPost().set_data(json=request_body).run().validate('status_code', 200)

    def test_post_data(self):
        data = {"a": "1"}
        ApiHttpbinPost().set_data(data=json.dumps(data)).run().validate('status_code', 200)

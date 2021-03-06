import json

from tests.api.httpbin import *


class TestCore:

    def test_get(self):
        ApiHttpbinGet().run().validate('status_code', 200).validate('url', 'https://httpbin.org/get')

    def test_get_params(self):
        ApiHttpbinGet().set_params(abc=123, xyz=345).run()\
            .validate('headers.Content-Type', 'application/json')\
            .validate("json().url","https://httpbin.org/get?abc=123&xyz=345")\
            .validate("json().headers.Host","httpbin.org")

    def test_post_json(self):
        request_body = {"a": "1"}
        ApiHttpbinPost().set_data(json=request_body).run()\
            .validate('status_code', 200) \
            .validate("json().data", '{"a": "1"}')

    def test_post_data(self):
        data = {"a": "1"}
        ApiHttpbinPost().set_data(data=json.dumps(data)).run()\
            .validate('status_code', 200) \
            .validate("json().json.a", '1')

    def test_get_cookie(self):
        cookies = {"cookie": "abc"}
        ApiHttpbinGetCookies().set_cookie(cookies).run().validate("json().cookies.cookie","abc")

    def test_extract(self):
        cookies = {"cookie": "abc"}
        assert ApiHttpbinGetCookies().set_cookie(cookies).run().extract("json().cookies.cookie") == "abc"

    def test_httpbin_login_status(self):
        # step 1:login in and set cookie  ?freeform=123
        ApiHttpbinSetCookies().set_params(freeform=123).run()

        # step 2:call other api and has step1's cookies in its headers
        resp = ApiHttpbinPost().set_data(json={'abc':'123'}).run().get_response()
        assert 'freeform=123' in resp.request.headers['Cookie']
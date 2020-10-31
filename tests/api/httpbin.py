from AATestingApi.basic_api import BasicApi

# 这里都是接口的描述
# 这里不需要写params、data、json这几个参数，basicApi中有封装注入这几个参数的方法


class ApiHttpbinGet(BasicApi):
    url = "https://httpbin.org/get"
    method = "GET"
    headers = {"accept": "application/json"}



class ApiHttpbinPost(BasicApi):
    url = "https://httpbin.org/post"
    method = "POST"
    headers = {"accept": "application/json"}


class ApiHttpbinGetCookies(BasicApi):
    url = "https://httpbin.org/cookies"
    method = "GET"
    headers = {"accept": "application/json"}

class ApiHttpbinSetCookies(BasicApi):
    url = "https://httpbin.org/cookies/set"
    method = "GET"
    headers = {"accept": "text/plain"}
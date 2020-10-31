import requests

# 基类：封装 发起请求、校验结果、提取response的参数

session = requests.sessions.session()

class BasicApi:
    url = None
    method = None
    headers = None
    params = None
    data = None
    json = None
    cookies = None
    response = None

    # todo
    # 可以把所有注入参数的方法封装一下，前面是注入的参数名，后面是注入的参数值
    # def inject(self,key,value):
    # 如果能一次函数注入多个值就好了
    # 测试case输入参数的大小写需要兼容一下
    #  elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):  这句到底是用来干什么的？

    def set_cookie(self, cookie):
        self.cookies = cookie
        return self

    def extract(self):
        # 提取参数用于其他case
        # todo
        pass

    def set_params(self, **kwargs):
        '''
        用来处理有params的请求
        :param kwargs: 请求参数, **kwargs传入的必须是【xxx=xxx】的格式
        :return: 实例自身，用于级联操作
        '''
        self.params = kwargs.items()
        return self

    def set_data(self, **kwargs):
        """
        用来处理post请求的请求体，而且为了保持在test case里调用的级联格式一致性，这里专门写一个注入请求体的方法，返回self对象
        :param kwargs: post请求的请求体, **kwargs传入的必须是【json={xxx:yyy}】或者【data="xxxx"】的格式
        :return: 实例自身，用于级联操作
        """
        for k, v in kwargs.items():
            if 'data' == k:
                self.data = v
            elif 'json' == k:
                self.json = v
        return self

    def run(self):
        """
        发送requests请求
        :return: 实例自身，用于级联操作
        """
        self.response = session.request(self.method, self.url, headers=self.headers, params=self.params,
                                         cookies=self.cookies,
                                         data=self.data, json=self.json)
        return self

    def validate(self, key, excepted_value):
        """
        用于断言
        :return: 实例自身，用于级联操作
        """
        acture_value = self.extract(key)
        assert acture_value == excepted_value
        return self

    def extract(self,key):
        """
        解析传入的参数，返回response里对应的值
        :param key:
        :return:
        """
        value = self.response
        for _key in key.split('.'):
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = value.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]
        return value

    def get_response(self):
        return self.response
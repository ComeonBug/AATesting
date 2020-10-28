
class BasicApi:
    url = None
    method = None
    headers = {"accept": "application/json"}
    params = {}
    data = None
    json = None

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
        self.response = requests.request(self.method, self.url, headers=self.headers, params=self.params,
                                         data=self.data, json=self.json)
        return self

    def validate(self, key, excepted_value):
        """
        用于断言
        :return: 实例自身，用于级联操作
        """
        actual_value = getattr(self.response, key)
        assert actual_value == excepted_value
        return self
class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)
        # self.asf = 0

    def __getattr__(self, name):
        '''
           例:init里没有asf属性,就自动调用此方法
        '''
        print(name)
        value =  self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
            # print("s")
        return value

if __name__ == '__main__':
    od = ObjectDict(asf={'a': 1}, d=True)
    print("__main__:",od.asf,od.asf.a)
    print()
    # a = {'b':2}
    # print(a)
    # print(od.d)
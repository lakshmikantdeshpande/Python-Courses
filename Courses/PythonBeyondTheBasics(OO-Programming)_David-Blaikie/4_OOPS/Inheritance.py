class Date(object):
    def get_date(self):
        return '2017-11-7'

    def hello(self):
        print("Hello, I'm a parent")


class Time(Date):
    def get_time(self):
        return '02:51:17'

    def hello(self):
        print("Hello, I'm a child")


dt = Date()
print(dt.get_date())
dt.hello()

print()

tm = Time()
print(tm.get_time())
print(tm.get_date())
tm.hello()

def calculate(**kwargs):
    print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["a"])


calculate(a=4, b=5, c=7)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="nissan", model="gtr")
print(my_car.model)

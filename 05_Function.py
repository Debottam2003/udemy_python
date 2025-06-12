# from module1.m1py import do
from m1py import do
print("Let's learn all about function")
name = "debottam"
def printName(name):
    print(name)

# decorator function
def my_decorator(function):
    req = {"body": "this is the request body"}
    def say_hello():
        print(req)
        function()
    return say_hello

if __name__ == "__main__":
    printName(name)
    do()
    @my_decorator #say_hello = my_decorator(say_hello)
    def say_hello():
        print("hello from debottam.")
    say_hello()
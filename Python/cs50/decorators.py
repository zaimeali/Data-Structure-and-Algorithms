def announce(f):
    def wrapper():
        print("About to run")
        f()
        print("Done running")
    return wrapper


@announce
def hello():
    print("Hello World")


hello()

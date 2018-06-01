from importlib import import_module

if __name__ == "__main__":
    module = import_module('.hello', 'hello')
    print(module.hello())
    print(module.get_package())

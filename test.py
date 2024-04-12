import importlib.util

class MyClass:
    def __init__(self):
        self.func = None
        self.set_func("eth")

    def set_func(self, mname):
        print("Module name:", mname)  # Add this line to check the module name
        try:
            spec = importlib.util.spec_from_file_location(mname, f"coinspecific/{mname}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self.func = getattr(module, 'checkBalance')
        except FileNotFoundError:
            print(f"Module {mname} not found.")
        except AttributeError:
            print(f"Function checkBalance not found in module {mname}.")

# Example usage
my_instance = MyClass()
# my_instance.set_func("eth")

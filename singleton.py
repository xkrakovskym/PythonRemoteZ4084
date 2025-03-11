class ConfigSingleton:
    _instance = None

    def __init__(self):
        print("Calling init")
        self.value = None

    def __new__(cls):
        print("Calling New")
        if cls._instance is None:
            print("Allocating memory")
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            cls._instance.value = "Default Configuration"
        return cls._instance


config1 = ConfigSingleton()
config2 = ConfigSingleton()

print(config1 == config2)

class Light:
    @staticmethod
    def on():
        print("The light is on")

    @staticmethod
    def off():
        print("The light is off")


class Thermostat:
    def __init__(self, temperature):
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Setting temperature to {temperature}")

class SecuritySystem:
    @staticmethod
    def activate():
        print("The security alarm activated")

    @staticmethod
    def deactivate():
        print("The security alarm was deactivated")


class HomeAutomationFacade:
    def __init__(self, light, thermostat, security_system):
        self.light = light
        self.thermostat = thermostat
        self.security_system = security_system

    def leave_home(self):
        print("leaving home")
        self.light.off()
        self.thermostat.set_temperature(18)
        self.security_system.activate()

    def arrive_home(self):
        self.security_system.deactivate()
        self.light.on()
        self.thermostat.set_temperature(22)



home_automation = HomeAutomationFacade(Light(), Thermostat(20), SecuritySystem())

home_automation.leave_home()
home_automation.arrive_home()
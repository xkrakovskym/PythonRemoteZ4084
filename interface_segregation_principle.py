from abc import ABC, abstractmethod

class BadPrinter(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class XeroxPrinter(BadPrinter):
    def print(self, document):
        print(document)


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldXeroxPrinter(Printer):
    def print(self, document):
        print(document)


class NewPrinter(Printer, Fax):
    def print(self, document):
        print(document)

    def fax(self, document):
        pass


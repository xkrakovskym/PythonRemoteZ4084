class BadMySQLDatabase:
    def connect(self):
        print("Connecting to MySQL database...")

    def fetch_data(self):
        return {"Name": "Alice", "Age": 30}


class BadReportGenerator:
    def __init__(self):
        self.database = BadMySQLDatabase()  # Direct dependency on a low-level module

    def generate(self):
        self.database.connect()
        data = self.database.fetch_data()
        return f"Report:\n" + "\n".join(
            [f"{key}: {value}" for key, value in data.items()]
        )


from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch_data(self):
        pass


class MySQLDatabase(DataSource):
    def connect(self):
        print("Connecting to MySQL database...")

    def fetch_data(self) -> dict:
        return {"Name": "Alice", "Age": 30}


class PostgreSQLDatabase(DataSource):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def fetch_data(self):
        return {"Name": "Bob", "Age": 25}


class ReportGenerator:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def generate(self):
        self.data_source.connect()
        data = self.data_source.fetch_data()
        return f"Report:\n" + "\n".join(
            [f"{key}: {value}" for key, value in data.items()]
        )


postgre_db = PostgreSQLDatabase()
report_generator = ReportGenerator(postgre_db)
report = report_generator.generate()
# print(report)

print("text".join(["1", "2", "3"]))

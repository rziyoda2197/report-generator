class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        report = ""
        for key, value in self.data.items():
            report += f"{key}: {value}\n"
        return report

    def generate_table_report(self):
        report = ""
        for key, value in self.data.items():
            report += f"| {key} | {value} |\n"
        return report

    def generate_json_report(self):
        import json
        return json.dumps(self.data)


# Misol
data = {
    "Sana": "2022-01-01",
    "Kiritilgan ma'lumotlar": 100,
    "Tayyor ma'lumotlar": 50,
    "Natija": 50
}

generator = ReportGenerator(data)
print(generator.generate_report())
print(generator.generate_table_report())
print(generator.generate_json_report())

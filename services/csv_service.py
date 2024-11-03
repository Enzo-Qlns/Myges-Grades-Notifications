import csv
from typing import List, Dict, Any


class CSVManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.fieldnames = [
            "course", "code", "grades", "bonus", "exam", "average", "trimester",
            "trimester_name", "year", "rc_id", "ects", "coef",
            "teacher_civility", "teacher_first_name", "teacher_last_name",
            "absences", "lates", "letter_mark", "ccaverage", "links", "id"
        ]

    def write_data(self, data: List[Dict[str, Any]]) -> None:
        """
        Ecris les éléments dans le fichier CSV
        :param data: Element à écrire
        :return: None
        """
        filtered_data = [{k: v for k, v in row.items() if k in self.fieldnames} for row in data]
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(filtered_data)

    def read_data(self) -> List[Dict[str, Any]]:
        """
        Lit les éléments du fichier CSV
        :return: List[Dict[str, Any]]
        """
        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def delete_all_grades(self) -> None:
        """
        Supprime tous les éléments du fichier CSV
        :return: None
        """
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows([])

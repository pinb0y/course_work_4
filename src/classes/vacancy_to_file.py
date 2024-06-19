import json
from abc import ABC, abstractmethod

from src.classes.vacancy import Vacancy


class VacancyToFile(ABC):
    """Интерфейс для классов сохранения вакансий в файл."""

    @abstractmethod
    def add_vacancy_list(self, link, vacancies):
        pass

    @abstractmethod
    def get_vacancy(self, link):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class VacancyToJSON(VacancyToFile):
    """Класс для сохранения вакансий в JSON файл"""

    def add_vacancy_list(self, link: str, vacancies: list[Vacancy]) -> None:
        """
        Добавляет список вакансий в JSON файл.
        :param link: Ссылка на файл
        :param vacancies: Список вакансий
        :return: None
        """
        data: list = []
        for vacancy in vacancies:
            data.append(vacancy)
        with open(link, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_vacancy(self, link: str) -> list[dict]:
        """
        Получает список вакансий из файла.
        :param link: Ссылка на файл.
        :return: Список вакансий.
        """
        with open(link, "r", encoding="utf-8") as file:
            temp = file.read()
            return json.loads(temp)

    def delete_vacancy(self):
        """Удаление Вакансии из списка. В разработке пока."""
        pass

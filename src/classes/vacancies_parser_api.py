from abc import ABC, abstractmethod

import requests


class VacanciesParserAPI(ABC):
    """Интерфейс для парсера вакансий."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        """Получить список вакансий по ключевому слову"""
        pass


class HeadHunterVacanciesParserAPI(VacanciesParserAPI):
    """Персер вакансий с сайта HeadHunter"""

    url: str
    headers: dict
    params: dict
    vacancies: list[dict]

    def __init__(self) -> None:
        """Конструктор класса"""
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "only_with_salary": True, "area": "113", "page": 0, "per_page": 100}
        self.vacancies = []

    def get_vacancies(self, keyword: str) -> None:
        """
        Получает сырой список вакансий по России по ключевому слову.
        :param keyword: Ключевое слово для поиска
        :return: список в json формате
        """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response: requests = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies: list[dict] = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

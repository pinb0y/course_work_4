import pytest

from src.classes.vacancies_parser_api import HeadHunterVacanciesParserAPI
from src.classes.vacancy import HeadhunterVacancy
from src.classes.vacancy_to_file import VacancyToJSON


@pytest.fixture
def make_parser():
    test_parser = HeadHunterVacanciesParserAPI()
    return test_parser


@pytest.fixture
def make_vacancy1():
    test_vacancy1 = HeadhunterVacancy("name1",
                                      "link1",
                                      "company1",
                                      "city1",
                                      "exp1",
                                      50000,
                                      0)
    return test_vacancy1


@pytest.fixture
def make_vacancy2():
    test_vacancy2 = HeadhunterVacancy("name2",
                                      "link2",
                                      "company2",
                                      "city2",
                                      "exp2",
                                      80000,
                                      100000)
    return test_vacancy2


@pytest.fixture
def make_vacancy3():
    test_vacancy3 = HeadhunterVacancy("name3",
                                      "link3",
                                      "company3",
                                      "city3",
                                      "exp3",
                                      0,
                                      0)
    return test_vacancy3


@pytest.fixture
def make_vacancy4():
    test_vacancy4 = HeadhunterVacancy("name4",
                                      "link4",
                                      "company4",
                                      "city4",
                                      "exp4",
                                      0,
                                      50000)
    return test_vacancy4
@pytest.fixture
def make_file_to_json():
    test_to_json = VacancyToJSON()
    return test_to_json

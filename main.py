from src.classes.vacancies_parser_api import HeadHunterVacanciesParserAPI
from src.classes.vacancy import HeadhunterVacancy
from src.classes.vacancy_to_file import VacancyToJSON
from src.settings import VACANCIES_JSON_PASS
from src.utils import sort_vacancies, print_top_n_vacancies, vacancy_salary_filter


def user_interaction():
    """
    Функция взаимодействия с пользователем.
    :return: None
    """

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    salary_range = input("Введите диапазон зарплат(например, 100000 - 120000): ")

    print()

    hh_parser = HeadHunterVacanciesParserAPI()
    hh_parser.get_vacancies(search_query)

    vacancies = hh_parser.vacancies

    vacancies_to_json = VacancyToJSON()
    vacancies_to_json.add_vacancy_list(VACANCIES_JSON_PASS, vacancies)

    vacancies_from_json = vacancies_to_json.get_vacancy(VACANCIES_JSON_PASS)

    vacancies_list = HeadhunterVacancy.make_object_list(vacancies_from_json)
    sorted_vacancies = sort_vacancies(vacancies_list)
    filtered_vacancies = vacancy_salary_filter(sorted_vacancies, salary_range)

    print_top_n_vacancies(top_n, filtered_vacancies)


if __name__ == "__main__":
    user_interaction()

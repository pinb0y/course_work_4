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

    search_query: str = input("Введите поисковый запрос: ")
    top_n: str = input("Введите количество вакансий для вывода(по умолчанию выводит все вакансии): ")

    while True:
        salary_range: str = input("Введите диапазон зарплат(например, 100000 - 120000): ")
        if "-" in salary_range:
            salary_range_list = [int(num.strip()) for num in salary_range.split('-')]
            if salary_range_list[0] <= salary_range_list[1]:
                break
        print("Некорректный диапазон")
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

    all_found_vacancies_quantity = len(filtered_vacancies)
    print(f"Всего {all_found_vacancies_quantity} вакансий \n")

    print_top_n_vacancies(top_n, all_found_vacancies_quantity,  filtered_vacancies)


if __name__ == "__main__":
    user_interaction()

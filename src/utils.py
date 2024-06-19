from src.classes.vacancy import HeadhunterVacancy


def sort_vacancies(vacancies: list[HeadhunterVacancy]) -> list[HeadhunterVacancy]:
    """
    Сортирует вакансии по увеличению зарплат "от".
    :param vacancies: Список объектов класса вакансия.
    :return: Отсортированный список объектов класса вакансия.
    """

    return sorted(vacancies)


def print_top_n_vacancies(quantity: str, all_vacancies: int, vacancies: list[HeadhunterVacancy]) -> None:
    """
    Выводит на экран заданное пользователем количество вакансий.
    :param all_vacancies: Общее количество вакансий
    :param quantity: Количество вакансий запрошенное пользователем.
    :param vacancies: Список объектов класса вакансия.
    :return: None
    """
    if quantity:
        quantity = int(quantity)
    else:
        quantity = all_vacancies
    for i in range(quantity):
        print(vacancies[i])


def vacancy_salary_filter(vacancies: list[HeadhunterVacancy], salary_range: str) -> list[HeadhunterVacancy]:
    """
    Фильтрует список объектов класса вакансия, согласно заданному диапазону зарплат.
    :param vacancies: Список объектов класса вакансия.
    :param salary_range: Заданный пользователем диапазон зарплат.
    :return: Отфильтрованный список объектов класса вакансия.
    """

    salary_range_list: list[int] = [int(num.strip()) for num in salary_range.split("-")]
    filtered_vacancies_list: list = []
    for vacancy in vacancies:
        if salary_range_list[0] <= vacancy.salary_from <= salary_range_list[1]:
            filtered_vacancies_list.append(vacancy)
    return filtered_vacancies_list

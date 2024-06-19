from src.utils import sort_vacancies, print_top_n_vacancies, vacancy_salary_filter


def test_sort_vacancies(make_vacancy1, make_vacancy2):
    assert sort_vacancies([make_vacancy1, make_vacancy2]) == [make_vacancy1, make_vacancy2]


def test_print_top_n_vacancies(make_vacancy1, make_vacancy2):
    assert print_top_n_vacancies("1",
                                 2,
                                 [make_vacancy1,
                                  make_vacancy2]) is None


def test_vacancy_salary_filter(make_vacancy2, make_vacancy1):
    assert vacancy_salary_filter([make_vacancy2, make_vacancy1], "40000 - 50000") == [make_vacancy1]

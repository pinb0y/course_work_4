from src.utils import sort_vacancies, print_top_n_vacancies


def test_sort_vacancies(make_vacancy1, make_vacancy2):
    assert sort_vacancies([make_vacancy1, make_vacancy2]) == [make_vacancy1, make_vacancy2]


def test_print_top_n_vacancies(make_vacancy1, make_vacancy2):
    assert print_top_n_vacancies("1",
                                 2,
                                 [make_vacancy1,
                                  make_vacancy2]) is None

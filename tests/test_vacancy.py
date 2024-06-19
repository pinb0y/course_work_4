def test_vacancy_no_salary_print(make_vacancy3):
    assert make_vacancy3.salary_print() == "Зарплата не указана"


def test_vacancy_salary_from_print(make_vacancy1):
    assert make_vacancy1.salary_print() == "от 50000"


def test_vacancy_salary_from_to_print(make_vacancy2):
    assert make_vacancy2.salary_print() == "от 80000 до 100000"


def test_vacancy_salary_to_print(make_vacancy4):
    assert make_vacancy4.salary_print() == "до 50000"

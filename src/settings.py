import pathlib

# корневой путь
ROOT_PATH = pathlib.Path(__file__).parent.parent

# путь к папке с файлами
DATA_PATH = ROOT_PATH.joinpath("data")

# путь к JSON файлу с вакансиями
VACANCIES_JSON_PASS = DATA_PATH.joinpath("vacancies.json")



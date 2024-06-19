import pathlib

# корневой путь
ROOT_PATH = pathlib.Path(__file__).parent.parent

# путь к папке с файлами
DATA_PATH = ROOT_PATH.joinpath("data")

# путь к JSON файлу с вакансиями
VACANCIES_JSON_PATH = DATA_PATH.joinpath("vacancies.json")

TEST_JSON_PATH = DATA_PATH.joinpath("test_data.json")

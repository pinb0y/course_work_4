from src.settings import TEST_JSON_PATH


def test_add_vacancy(make_file_to_json):
    assert make_file_to_json.get_vacancy(TEST_JSON_PATH) == [
        {
            "id": "100313010"
        }
    ]

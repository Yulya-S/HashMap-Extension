import pytest
from specialHashMap import SpecialHashMap


@pytest.fixture(scope="function")
def specialHashMap():
    return SpecialHashMap()


class TestSpecialHashMap:

    def test_iloc(self, specialHashMap):
        specialHashMap["value1"] = 1
        specialHashMap["1"] = 10
        assert specialHashMap.iloc[0] == 10

    def test_iloc_out_of_range(self, specialHashMap):
        specialHashMap["value1"] = 1
        with pytest.raises(ValueError):
            specialHashMap.iloc[1]

    @pytest.mark.parametrize(
        "text, response",
        [("=3", "{'3': 30}"),
         (">2", "{'3': 30}"),
         ("<4", "{'3': 30}"),
         (">=3", "{'3': 30}"),
         ("<=3", "{'3': 30}"),
         ("<>2", "{'3': 30}")]
    )
    def test_ploc(self,specialHashMap, text, response):
        specialHashMap["3"] = 30
        specialHashMap["value3"] = 30
        assert specialHashMap.ploc[text].__str__() == response

    def test_invalid_conditions(self, specialHashMap):
        specialHashMap["3"] = 30
        with pytest.raises(ValueError):
            specialHashMap.ploc["<<=3"]

    def test_incorrect_condition(self, specialHashMap):
        specialHashMap["3"] = 30
        with pytest.raises(ValueError):
            specialHashMap.ploc["dfgh"]

    def test_condition_without_number(self, specialHashMap):
        specialHashMap["3"] = 30
        with pytest.raises(ValueError):
            specialHashMap.ploc[">"]

    def test_condition_is_not_str(self, specialHashMap):
        specialHashMap["3"] = 30
        with pytest.raises(ValueError):
            specialHashMap.ploc[3]

    def test_empty_condition(self, specialHashMap):
        specialHashMap["3"] = 30
        with pytest.raises(ValueError):
            specialHashMap.ploc[""]





def get_countries():
    return {"Algeria": "ALG", "Albania": "ALB"}

def get_country_code(key, get_countries):
    countries = get_countries() # Dependency
    return countries[key]


print(get_country_code("Albania", get_countries))

def test_get_country_code():
    country = "Algeria"
    expected = "AL"

    def mock_get_countries():
        return {"Algeria": "AL"}

    result = get_country_code(country, mock_get_countries)

    assert expected == result

test_get_country_code()


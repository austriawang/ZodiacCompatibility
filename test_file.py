def test_zodiac_sign():
    assert zodiac_dates(4, 20, 5, 20) == "TAURUS ♉"
    assert zodiac_dates(5, 21, 6, 20) == "GEMINI ♊"
    assert zodiac_dates(6, 21, 7, 22) == "CANCER ♋"
    assert zodiac_dates(7, 23, 8, 22) == "LEO ♌"
    assert zodiac_dates(8, 23, 9, 22) == "VIRGO ♍"
    assert zodiac_dates(9, 23, 10, 22) == "LIBRA ♎"
    assert zodiac_dates(10, 23, 11, 21) == "SCORPIO ♏"
    assert zodiac_dates(11, 22, 12, 21) == "SAGITTARIUS ♐"
    assert zodiac_dates(12, 22, 1, 19) == "CAPRICORN ♑"
    assert zodiac_dates(1, 20, 2, 18) == "AQUARIUS ♒"
    assert zodiac_dates(2, 19, 3, 20) == "PISCES ♓"


def test_zodiac_compatibility():
    assert isinstance(zodiac_compatibility(type), str)
    assert zodiac_compatibility("TAURUS ♉") == {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"}
    assert zodiac_compatibility("GEMINI ♊") == {"GEMINI ♊", "LIBRA ♎", "AQUARIUS ♒", "ARIES ♈", "LEO ♌", "SAGITTARIUS ♐"}
    assert zodiac_compatibility("CANCER ♋") == {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"}
    assert zodiac_compatibility("LEO ♌") == {"ARIES ♈", "LEO ♌", "SAGITTARIUS ♐", "LIBRA ♎", "GEMINI ♊", "AQUARIUS ♒"}
    assert zodiac_compatibility("VIRGO ♍") == {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"}
    assert zodiac_compatibility("LIBRA ♎") == {"GEMINI ♊", "LIBRA ♎", "AQUARIUS ♒", "ARIES ♈", "LEO ♌", "SAGITTARIUS ♐"}
    assert zodiac_compatibility("SCORPIO ♏") == {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"}
    assert zodiac_compatibility("SAGITTARIUS ♐") == {"GEMINI ♊", "LIBRA ♎", "AQUARIUS ♒", "ARIES ♈", "LEO ♌", "SAGITTARIUS ♐"}
    assert zodiac_compatibility("CAPRICORN ♑") == {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"}
    assert zodiac_compatibility("AQUARIUS ♒") == {"GEMINI ♊", "LIBRA ♎", "AQUARIUS ♒", "ARIES ♈", "LEO ♌", "SAGITTARIUS ♐"}
    assert zodiac_compatibility("PISCES ♓") == {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"}

    
def test_random_birthdays():
    random_birthdays = {
        'iris': (7, 5),
    'christiana': (9, 2),     
    'austria': (9, 28),  
    'ethan': (11, 19),  
    'david': (7, 7),
    'naomi': (2, 13),  
    'james': (7, 15), 
    'richard': (5,8),
    'lorain': (7, 19),   
    'kelly': (2, 21),
    'yanni': (12, 4),  
    'leen': (5, 9), 
    'kristine': (7, 5), 
    'sarah': (12, 26),
    'kylie': (7, 26), 
    'clarissa': (12, 10), 
    'olivia': (10, 8),
    'johnny': (11, 9),
    'sofia': (12, 26),
    'emily': (7, 21)
    } 
    for key, value in random_birthdays.items():
        assert isinstance(key, str)
        assert isinstance(value, tuple)
        assert len(value) == 2
        assert isinstance(value[0], int)
        assert isinstance(value[1], int)

def zodiac_sign(month, day):
    """Using user inputted birth month and date to determine zodiac sign.
    
        month: integer
            to be inputted by user
        date: integer
            to be inputted by user
            
        Return:
        answer: string
        The user's zodiac sign is determined by their birth month and birth day.
    """
    zodiac_dates = [
        (3, 21, 4, 19, "ARIES ♈"),
        (4, 20, 5, 20, "TAURUS ♉"),
        (5, 21, 6, 20, "GEMINI ♊"),
        (6, 21, 7, 22, "CANCER ♋"),
        (7, 23, 8, 22, "LEO ♌"),
        (8, 23, 9, 22, "VIRGO ♍"),
        (9, 23, 10, 22, "LIBRA ♎"),
        (10, 23, 11, 21, "SCORPIO ♏"),
        (11, 22, 12, 21, "SAGITTARIUS ♐"),
        (12, 22, 1, 19, "CAPRICORN ♑"),
        (1, 20, 2, 18, "AQUARIUS ♒"),
        (2, 19, 3, 20, "PISCES ♓")
    ]

    for start_month, start_day, end_month, end_day, sign in zodiac_dates:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign

    return "NOT VALID BIRTHDAY"
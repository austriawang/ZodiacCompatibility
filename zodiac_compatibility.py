def zodiac_compatibility(sign_first, sign_second):
    """Compare two zodiac signs togther for compatibility.
    
        sign_first : string
            zodiac signs are stored in zodiac_signs.py module
        sign_second : string
            zodiac signs are stored in zodiac_signs.py module
        
        Returns: 
        answer: string
        Whether the two zodiac signs are compatibility or not. 
    """
    compatibility = {
        "ARIES ♈": {"ARIES ♈", "LEO ♌", "SAGITTARIUS ♐", "LIBRA ♎", "GEMINI ♊", "AQUARIUS ♒"},
        "TAURUS ♉": {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"},
        "GEMINI ♊": {"GEMINI ♊", "LIBRA ♎", "AQUARIUS ♒", "ARIES ♈", "LEO ♌", "SAGITTARIUS ♐"},
        "CANCER ♋": {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"},
        "LEO ♌": {"ARIES ♈", "LEO ♌", "SAGITTARIUS ♐", "LIBRA ♎", "GEMINI ♊", "AQUARIUS ♒"},
        "VIRGO ♍": {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"},
        "LIBRA ♎": {"GEMINI ♊", "LIBRA ♎", "AQUARIUS ♒", "ARIES ♈", "LEO ♌", "SAGITTARIUS ♐"},
        "SCORPIO ♏": {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"},
        "SAGITTARIUS ♐": {"GEMINI ♊", "LIBRA ♎", "AQUARIUS ♒", "ARIES ♈", "LEO ♌", "SAGITTARIUS ♐"},
        "CAPRICORN ♑": {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"},
        "AQUARIUS ♒": {"GEMINI ♊", "LIBRA ♎", "AQUARIUS ♒", "ARIES ♈", "LEO ♌", "SAGITTARIUS ♐"},
        "PISCES ♓": {"TAURUS ♉", "VIRGO ♍", "CAPRICORN ♑", "CANCER ♋", "SCORPIO ♏", "PISCES ♓"},
    }

    if sign_first in compatibility and sign_second in compatibility[sign_first]:
        return "you two are compatible 💕"
    else:
        return "you two may not be fully compatible 💔"

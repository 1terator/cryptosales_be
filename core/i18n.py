import gettext

DEFAULT_LANGUAGE = "en"


def translate_for_user(message: str, language: str = DEFAULT_LANGUAGE) -> str:
    return gettext.translation(
        "base", localedir="locales/", languages=[language]
    ).gettext(message)

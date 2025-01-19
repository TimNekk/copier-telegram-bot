import re
from packaging.version import parse, InvalidVersion

from jinja2.ext import Extension

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
SLUG_REGEX = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def is_valid_email(value):
    return re.match(EMAIL_REGEX, value)


def is_valid_version(value):
    try:
        parse(value)
        return True
    except InvalidVersion:
        return False


def is_valid_slug(value):
    return re.match(SLUG_REGEX, value)


class IsValidExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["is_valid_email"] = is_valid_email
        environment.filters["is_valid_version"] = is_valid_version
        environment.filters["is_valid_slug"] = is_valid_slug

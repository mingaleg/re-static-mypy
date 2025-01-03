__version__ = "0.0.0"
__version_tuple__ = (0, 0, 0)

# from re import Pattern as _Pattern, compile as _compile
# from typing import Annotated, AnyStr
# from typing_extensions import TypeAlias


# _static = object()
# Pattern: TypeAlias = Annotated[_Pattern[AnyStr], _static]


# def compile(
#     pattern: AnyStr,
#     flags: int = 0,
# ) -> Pattern[AnyStr]:
#     return _compile(pattern=pattern, flags=flags)


def some_function() -> str:
    """
    Some function docstring

    :return: Some string
    :rtype: str
    """
    return "some_variable_to_test"

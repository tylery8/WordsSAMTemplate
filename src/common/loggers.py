import json
import logging
from time import time
from functools import wraps
from typing import Type


def _convert_to_json_serializable(obj, depth=0, max_depth=10):
    if depth > max_depth:
        return None

    if isinstance(obj, (list, tuple)):
        return [_convert_to_json_serializable(item, depth + 1, max_depth) for item in obj]
    elif isinstance(obj, set):
        return [_convert_to_json_serializable(item, depth + 1, max_depth) for item in obj]
    elif isinstance(obj, dict):
        return {key: _convert_to_json_serializable(value, depth + 1, max_depth) for key, value in obj.items()}
    elif isinstance(obj, type):
        return f'Type[{obj.__name__}]'
    elif hasattr(obj, '__dict__'):
        return _convert_to_json_serializable(obj.__dict__, depth + 1, max_depth)

    try:
        json.dumps(obj)
        return obj
    except TypeError:
        return str(obj)


class Loggers:
    LOGGERS = {}

    @classmethod
    def get_logger(cls, for_class: Type):
        if for_class.__name__ not in cls.LOGGERS:
            cls.LOGGERS[for_class.__name__] = logging.getLogger(for_class.__name__)
            cls.LOGGERS[for_class.__name__].setLevel(level=logging.INFO)

        return cls.LOGGERS[for_class.__name__]

    @classmethod
    def auto_log(cls, for_class: Type):
        def log_inputs_outputs():
            def decorator(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    try:
                        cls.get_logger(for_class).info(json.dumps(dict(
                            function=f'{for_class.__name__}::{func.__name__}',
                            input=_convert_to_json_serializable({**dict(enumerate(args[1:])), **kwargs})
                        )))
                    except Exception as e:
                        cls.get_logger(for_class).warning(
                            f'{for_class.__name__}::{func.__name__} failed to log input: {e}')

                    start_time = time()
                    result = func(*args, **kwargs)
                    end_time = time()

                    try:
                        cls.get_logger(for_class).info(json.dumps(dict(
                            function=f'{for_class.__name__}::{func.__name__}',
                            duration=end_time - start_time,
                            output=_convert_to_json_serializable(result)
                        )))
                    except Exception as e:
                        cls.get_logger(for_class).warning(
                            f'{for_class.__name__}::{func.__name__} failed to log output: {e}')

                    return result
                return wrapper
            return decorator

        for attr_name, attr_value in vars(for_class).items():
            if callable(attr_value) and not attr_name.startswith("_"):
                setattr(for_class, attr_name, log_inputs_outputs()(attr_value))
        return for_class

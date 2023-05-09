'''This module contains a miscellaneous collection of unit functions.'''

import json
from typing import Any
from uuid import UUID
from decimal import Decimal
from datetime import date, datetime
from caseconverter import camelcase


class AppSettings():
    '''Application settings class.'''

    def __init__(self, d):
        for k, v in d.items():
            if isinstance(k, (list, tuple)):
                setattr(self, k, [AppSettings(x) if isinstance(x, dict) else x for x in v])
            else:
                setattr(self, k, AppSettings(v) if isinstance(v, dict) else v)


class DataFormatter:
    '''Data formatter class.'''

    def camel_case(s: str) -> str:
        '''Convert a string case to camel style.'''
        return camelcase(s)

    def postgresql(s: str) -> str:
        '''Format PostgreSQL URI string.'''
        if 'postgresql' not in s:  # pylint: disable=[E1135]
            return s.replace('postgres', 'postgresql')
        return s


class FileManagement:
    '''File management class.'''

    def read_file(filename: str) -> str | dict | None:
        '''Read HTML, JSON, SQL, and TXT files.'''
        _type = filename.split('.')[-1]
        with open(filename, mode='r', encoding='utf-8') as f:
            if _type in ['html', 'sql', 'txt']:
                return f.read()
            if _type == 'json':
                return json.load(f)
        return None

    def write_file(filename: str, data: str | dict) -> None:
        '''Write CSV, HTML, JSON, SQL, and TXT files.'''
        _type = filename.split('.')[-1]
        with open(filename, 'w', encoding='utf-8') as f:
            if _type in ['html', 'sql', 'txt']:
                f.write(data)
            if _type == 'json':
                json.dump(data, f, indent=4)


class JSONCustomEncoder(json.JSONEncoder):
    '''JSON custom encoder class.'''

    def default(self, o: Any) -> str | float:
        '''JSON serializer for objects not serializable by default json code.'''
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if isinstance(o, Decimal):
            return float(o)
        if isinstance(o, UUID):
            return o.hex
        return super().default(o)


class ResponseFormatter:
    '''HTTP Response formatter class.'''

    def obj_list_to_camel_case(data: list) -> list:
        '''Convert the keys of a list of dictionaries to camel style.'''
        for d in data:  # pylint: disable=[E1133]
            for k in list(d.keys()):
                d[DataFormatter.camel_case(k)] = d.pop(k)
        return data

    def obj_list_strip_string(data: list) -> list:
        '''Remove the leading and the trailing characters of the string values of a list of dictionaries.'''
        for d in data:  # pylint: disable=[E1133]
            for k, v in d.items():
                if isinstance(v, str):
                    d[k] = v.strip()
        return data


class TextColor:
    '''ANSI color codes.'''

    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    CLOSURE = '\033[00m'


# Calling functions
def try_except(func, *args, **kwargs):
    '''Generic try-except function.'''
    try:
        return func(*args, **kwargs)
    except Exception as e:  # noqa: F841 pylint: disable=[W0612,W0703]
        return None

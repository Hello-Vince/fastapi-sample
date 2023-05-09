'''This module configures application settings from config.yaml'''

from pyaml_env import parse_config
from dotenv import load_dotenv

from helpers.misc import AppSettings, DataFormatter
from helpers.lru_caching import timed_lru_cache


load_dotenv()


@timed_lru_cache(seconds=60)
def get_settings() -> AppSettings:
    '''Set up settings in cache for the above lifetime, then refreshes it.'''
    return AppSettings(config)


# project settings
config = parse_config('config.yaml')

# set up API prefix
version = config['APP']['PROJECT_VERSION']
config['API'] = {}
config['API']['PREFIX'] = f'/api/v{version.split(".")[0]}'


# set up environment
if config['APP']['ENVIRONMENT'] == 'development':
    config['APP']['DEBUG'] = True
    config['APP']['TESTING'] = True

# set up database
config['DATABASE']['BASE_URL'] = DataFormatter.postgresql(config['DATABASE']['BASE_URL'])

from scrapy.exceptions import NotConfigured as NotConfigured, ScrapyDeprecationWarning as ScrapyDeprecationWarning
from scrapy.settings import Settings as Settings
from scrapy.utils.conf import closest_scrapy_cfg as closest_scrapy_cfg, get_config as get_config, init_env as init_env

ENVVAR: str
DATADIR_CFG_SECTION: str

def inside_project(): ...
def project_data_dir(project: str = ...): ...
def data_path(path, createdir: bool = ...): ...
def get_project_settings(): ...

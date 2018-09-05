# coding: utf-8
"""全局配置"""

import os
import json
import logging.config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 读取数据库配置文件
config_file = os.path.join(BASE_DIR, '.env')
CONFIG_INFO = {}  # 项目配置参数
try:
    if os.path.isfile(config_file):
        config = open(config_file).read()
        config = json.loads(config)
        CONFIG_INFO = config
except Exception, ex:
    print 'load .env config error=%s' % ex

if CONFIG_INFO:
    DEBUG = True if CONFIG_INFO.get("DEBUG") == "True" else False
else:
    DEBUG = True

# 阿里云日志服务
# 运维平台需添加SLS关系和增加私有配置SLS_STORE=python、SLS_TOPIC=项目唯一标识(同下)
# 项目唯一标识：例如lsjm_service项目的give_book服务可标记为lsjm_service.give_book或lsjm_service，便于区分查询日志
# 需安装pip包  aliyun-log-python-sdk和uwsgidecorators
if CONFIG_INFO:
    ALI_SLS_ENDPOINT = CONFIG_INFO['SLS_ENDPOINT']
    ALI_SLS_ACCESSID = CONFIG_INFO['SLS_ACCESSID']
    ALI_SLS_ACCESSKEY = CONFIG_INFO['SLS_ACCESSKEY']
    ALI_SLS_PROJECT = CONFIG_INFO['SLS_PROJECT']
    ALI_SLS_STORE = CONFIG_INFO['SLS_STORE']
    ALI_SLS_TOPIC = CONFIG_INFO['SLS_TOPIC']
else:
    # ALI_SLS_ENDPOINT = 'cn-beijing.log.aliyuncs.com'
    # ALI_SLS_ACCESSID = 'LTAIIRXSEMJHVOoc'
    # ALI_SLS_ACCESSKEY = 'GAvjKsNoQ33mLpwrWE5Nx8p0ktPgLv'
    # ALI_SLS_PROJECT = 'uhong-test'
    # ALI_SLS_STORE = 'python'
    # ALI_SLS_TOPIC = 'lsjm_service.give_book'    # 此设置为项目唯一标识
    ALI_SLS_ENDPOINT = 'cn-shanghai.log.aliyuncs.com'
    ALI_SLS_ACCESSID = 'LTAIxcwvgUb8B6qR'
    ALI_SLS_ACCESSKEY = 'PslEXAQhuly6rQ1fv1g7YzVCEEGOAb'
    ALI_SLS_PROJECT = 'song'
    ALI_SLS_STORE = 'singsing'
    ALI_SLS_TOPIC = 'lsjm_service.give_book'    # 此设置为项目唯一标识

# 日志配置
LOGDIR = os.path.join(BASE_DIR, "log")
if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)  # 创建路径

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'default_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGDIR, 'app.log'),  # 或者直接写路径：'c:\logs\all.log',
            'mode': 'w+',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'aliyun_handler': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'aliyun.log.QueuedLogHandler',
            # 'class': 'aliyun.log.SimpleLogHandler',   # 支持uwsgi，极端情况下测试使用，不推荐生成环境使用
            'access_key_id': ALI_SLS_ACCESSID,
            'access_key': ALI_SLS_ACCESSKEY,
            'end_point': ALI_SLS_ENDPOINT,
            'project': ALI_SLS_PROJECT,
            'log_store': ALI_SLS_STORE,
            'topic': ALI_SLS_TOPIC,
            'extract_json': True,
        },
    },
    'loggers': {
    },
    "root": {
        'handlers': ['default_handler', 'console_handler', 'aliyun_handler'] if DEBUG else ['default_handler', 'aliyun_handler'],
        'level': "DEBUG" if DEBUG else "INFO",
        'propagate': False
    }
}

logging.config.dictConfig(LOGGING)

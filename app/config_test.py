# -*- coding: utf-8 -*-
DEBUG = True
TESTING = True
DATABASE_URI = 'mysql+pymysql://root:root@mysql/git_webhook'

CELERY_BROKER_URL = 'redis://:@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:@redis:6379/0'

GITHUB_CLIENT_ID = 'b6e751cc48d664240467'
GITHUB_CLIENT_SECRET = '6a9e0cbeee1bf89a1e1a25958f35b9dc6b36c996'

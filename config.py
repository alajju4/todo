import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
#플라스크 기본 시크릿키
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#db관련
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#페이지당 포스트 수
    PROJECTS_PER_PAGE = 7
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = bb'.\xa2\xe1\xd9\xd1\xd10\x16\xb7\xe3\xcf\xab\xb2r\xe2\x0f'

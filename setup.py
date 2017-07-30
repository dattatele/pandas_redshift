from setuptools import setup

setup(
    name = 'pandas_redshift',
    version = '0.1',
    scripts = ['pandas_redshift'],
    author = 'Aidan Gawronski',
    author_email = 'aidangawronski@gmail.com',
    url = 'https://github.com/agawronski/pandas_redshift',
    install_requires = ['traceback',
                        'psycopg2',
                        'pandas',
                        'boto3',
                        'sys',
                        'os',
                        'io']
)
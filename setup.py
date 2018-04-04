import os
from setuptools import setup, find_packages


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='pymysqlpool-dd',
    version='0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='Christopher Lee',
    author_email='',
    requires=['pymysql'],
    description='MySQL connection pool utility.',
)
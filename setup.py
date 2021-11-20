import sys
import os
from setuptools import setup, find_packages

setup(
    name='jigsaw-toxic-comments-cls-BERT',
    version='0.1.0',
    author='BachNG',
    author_email='nlmbao2015@gmail.com',
    packages=find_packages(exclude=['tests*']),
    # url='http://pypi.python.org/pypi/luxai2021/',
    description='Use bert model for toxic comments classification',
    install_requires=[
    ],
)


if sys.version_info < (3,7) or sys.version_info >= (3,8):
    os.system("")
    class style():
        YELLOW = '\033[93m'
    version = str(sys.version_info.major) + "." + str(sys.version_info.minor)
    message = f'/!\ Warning, python{version} detected, you will need to use python3.7 to submit to kaggle.'
    message = style.YELLOW + message
    print(message)
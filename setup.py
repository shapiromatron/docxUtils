from setuptools import setup
import re


def get_version():
    regex = r"""^__version__ = '(.*)'$"""
    with open('docxUtils/__init__.py', 'r') as f:
        text = f.read()
    return re.findall(regex, text, re.MULTILINE)[0]


setup(
    name='docxUtils',
    version=get_version(),
    description='Utility functions for python-docx library',
    long_description=open('README.rst').read(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    author='Andy Shapiro',
    author_email='shapiromatron@gmail.com',
    url='http://github.com/shapiromatron/docxUtils',
    license='MIT',
    packages=['docxUtils'],
    install_requires=['python-docx>=0.8.6'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

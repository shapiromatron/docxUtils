from setuptools import setup

version = '0.0.1'

setup(name='docxUtils',
      version=version,
      description='Utility functions for python-docx library',
      long_description=open('README.md').read(),
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      author='Andy Shapiro',
      author_email='shapiromatron@gmail.com',
      url='http://github.com/shapiromatron/docxUtils',
      license='MIT',
      py_modules=['docxUtils'],
      install_requires=['python-docx>=0.8.5']
)

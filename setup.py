from setuptools import setup, find_packages
import os

version = '1.0a1.dev0'

long_description = (
    open("README.rst").read() + "\n" +
    open(os.path.join("docs", "MANUAL.txt")).read() + "\n" +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    open("CHANGES.txt").read())

setup(name='raptus.article.accordeon',
      version=version,
      description="Provides an article listing displayed as an accordeon",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['raptus', 'raptus.article'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'raptus.article.core',
          'raptus.article.nesting',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

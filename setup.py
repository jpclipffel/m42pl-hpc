from setuptools import setup, find_packages


setup(
  name='m42pl-hpc',
  author='@jpclipffel',
  url='https://github.com/jpclipffel/m42pl-hpc',
  version='1.0.0',
  packages=find_packages(),
  install_requires=[
      'm42pl',
      'm42pl-encoders',
      'mpi4py'
  ]
)

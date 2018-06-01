from setuptools import setup

setup(name='testapp',
      version='1.0',
      description='testapp Application',
      author='Natrayan',
      author_email='',
      url='http://www.python.org/sigs/distutils-sig/',
     install_requires=['Flask>=0.7.2', 'MarkupSafe' , 'gunicorn>=0.19'],
     )

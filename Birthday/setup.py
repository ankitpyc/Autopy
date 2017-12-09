from setuptools import setup,find_packages
from distutils.sysconfig import get_python_inc
from setuptools.command.develop import develop
from setuptools.command.install import install
import base64
import os
import subprocess

setup(name='BirthdayFb',
      version='0.1',
      description='Schedule your Birthday wishes for your facebook friends and never Miss any birthdays',
      url='https://github.com/ankitpyc/Autopy/tree/master/Facebook_BirthdayWish_/Fb_Birthday',
      author='Ankit Mishra',
      author_email='ankitmishra@gmail.com',
      license='MIT',	
      entry_points={
        'console_scripts': ['FbWish = FaceBir.Happy:main','FbWishSettings = FaceBir.UpdateCred:Update'],
          },
      packages=find_packages(),  
      install_requires=['python-crontab','click'],
      zip_safe=True)

from setuptools import setup,find_packages
import sys, os

setup(
   name='tcpClientServer',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=find_packages(),
   namespace_packages=['client', 'server'],
   install_requires=[],
)

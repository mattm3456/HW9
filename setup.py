from setuptools import setup, find_packages

setup(
    name='BookLover',
    version='1.0.0',
    url='https://github.com/mattm3456/HW9',
    author='Matt Manner',
    author_email='xkv3na@virginia.edu',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'pandas >= 1.4.3'],
)
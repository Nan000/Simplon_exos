from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    content = f.readlines()
    requirements = [x.strip() for x in content if 'git+' not in x]

setup(
    name='rent',
    version='0.0.0.1',
    packages=find_packages(),
    description="Creation automatisé d'une architecture ML",
    author="Nariné Asatrian",
    author_email="n.asatrian93@gmail.com",
    scripts=['scripts/script_rent'],
    install_requires=requirements)
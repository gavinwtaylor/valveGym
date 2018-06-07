from setuptools import setup, find_packages

NAME='valveGym'
DESCRIPTION='for simulation of chemical plants'
AUTHOR='Gavin Taylor and Tom Adams'

setup(name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    version='0.0.1',
    install_requires=['gym','mpi4py'],  # And any other dependencies foo needs
    packages=find_packages(),
)  

from setuptools import setup

setup(name='valveGym',
      version='0.0.1',
      install_requires=['gym','mpi4py'],  # And any other dependencies foo needs
      packages=['valveGym','valveGym.envs'],
)  

from setuptools import setup, find_packages
from typing import List
HIPHON = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HIPHON in requirements:            requirements.remove(HIPHON)
    return requirements

setup(

  name='End-to-End-Ml-Project',
  version='0.0.1',
  author='Digambar Shukla',
  author_email='digambarshukla02@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')

)
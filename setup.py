from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This is a function to get the required packages from the requirements text file
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Ankit',
    author_email='dasankit194@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)
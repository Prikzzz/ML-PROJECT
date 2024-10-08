#respomsible in creating my machine learning project in oackage can be deployed in pypy
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup (
    name='ML Projects',
    version='0.0.1',
    author='Priyank',
    author_email='priyanks630@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )
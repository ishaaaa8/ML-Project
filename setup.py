from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requiremnets
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n","") for req in requirements]

        
setup(
    name='mlproject',
    version='0.0.1',
    author='Isha',
    author_email='itsisha4884@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
# install_requires=['numpy','pandas','seaborn'],
    # in many cases we do need many many packages so instead of above line , we create a function
from setuptools import setup,find_packages
from typing import List 


def get_requirements(file_path:str)->List[str]:
    """
    This functions return the List of requirements
    """

    requirements = []

    with open(file_path,'r') as file_obj:

        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

    return requirements


setup(
    name='laptop_price_predictor',
    version='0.0.1',
    author='Hanjala',
    author_email='hanzalasarang01@gmail.com',
    description="laptop price prediction",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
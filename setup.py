import pip
from setuptools import setup, find_packages

# Parse pip requirements from a requirements file
install_reqs = pip.req.parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]

config = {
    'author': 'Omar Eid',
    'author_email': 'omar_eid21@yahoo.com',
    'url': 'https://www.github.com/mr-uuid/datastructs',
    'name': "datastructs",
    'version': '0.1',
    'description': 'Data Structures in Python!',
    'packages': find_packages(),
    'install_requires': reqs,
    'scripts': [],
}

setup(**config)

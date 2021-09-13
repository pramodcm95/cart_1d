import setuptools

AUTHORS = [
    'Pramod Mahajan Chikkaballekere Manjunatha'
]

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cart_1d',
    version='1.0.0',
    packages=setuptools.find_packages(),
    install_requires=requirements,
)
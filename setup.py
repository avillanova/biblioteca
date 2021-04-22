from setuptools import find_packages, setup
setup(
    name='mypythonlib',
    version='0.1.1',
    description='My first Python library',
    author='Me',
    license='MIT',
    packages=find_packages(include=['mypythonlib'])
)
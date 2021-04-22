from setuptools import find_packages, setup
setup(
    name='biblioteca',
    version='0.0.3',
    description='My first Python library',
    author='Me',
    license='MIT',
    packages=find_packages(include=['mypythonlib'])
)
from setuptools import find_packages, setup


setup(
    name='myhead',
    version='1.0.0',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'Click~=8.1.2',
    ],
    entry_points={
        'console_scripts': [
            'myhead=myhead.core:cmd'
        ]
    }
)
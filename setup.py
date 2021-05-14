from setuptools import find_packages, setup

setup(
    name='work-measure-movies-viewing-time',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='mohira',
    author_email='mohira@example.com',
    description='',

    install_requires=[
        'Click',
    ],

    entry_points={'console_scripts': ['m=main:main']}
)

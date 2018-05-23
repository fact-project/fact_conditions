import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fact_conditions",
    version = "0.1.0",
    author = "Michael Bulinski",
    author_email = "michael.bulinski@udo.edu",
    description = ("Functions to load conditions for the fact quary. Also includes a veriety of given files."),
    license = "GPL3",
    keywords = "fact database query condition",
    url = "https://github.com/fact-project/fact_condition",
    packages=['fact_conditions'],
    long_description=read('README.md'),
    install_requires=[
        pyyaml,
        click,
        peewee
    ],
    package_data={'fact_conditions': ['conditions/*.yaml']},
    entry_points={
        'console_scripts': [
            'fact_create_condition_set = fact_conditions.createNewConditionSet:createNewConditionSet'
        ],
    },
)

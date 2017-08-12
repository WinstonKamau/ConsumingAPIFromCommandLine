'''A module to insert the setup tools and name the entry-points for commands'''
from setuptools import setup

setup(
    name="space",
    version="0.1",
    py_modules=["spacedata"],
    install_requires=[
        "Click",
    ],
    entry_points='''
    [console_scripts]
    space=spacedata:cli
    ''',
)

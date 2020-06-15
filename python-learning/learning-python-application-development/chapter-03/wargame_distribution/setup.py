from distutils.core import setup

with open("README") as file:
    readme = file.read()

setup(
    name="jawg_wargame",
    version="2.0.0",
    packages=["wargame"],
    url="https://testpypi.python.org/pypi/jawg_wargame",
    license="LICENSE.txt",
    description="my fantasy game",
    long_description=readme,
    author="johannes",
)

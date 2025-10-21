from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Gemini-Paper-Summary",
    version="0.1",
    author="Cll-The-Saint",
    packages=find_packages(),
    install_requires = requirements,
)
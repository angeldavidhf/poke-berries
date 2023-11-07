from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="poke-berries",
    version="0.1.0",
    description="Description",
    author="Angel David Hurtado Franco",
    author_email="angeldavidhf@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/angeldavidhf/pokeberries",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "requests",
        "matplotlib",
        "python-dotenv",
        "redis",
        "pytest"
    ]
)




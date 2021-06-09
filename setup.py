"""The python wrapper for Printful API package setup."""
from setuptools import (setup, find_packages)

setup(
    name="printful_api",
    version="1.0.1",
    packages=find_packages(),
    install_requires=["requests", "rich"],
    include_package_data=True,
    description="Printful API for Python",
    long_description="Printful API for Python",
    url="https://github.com/mdn522/printful-api-python",
    author="Abdullah Mallik",
    author_email="mdn522@gmail.com",
    zip_safe=False,
)

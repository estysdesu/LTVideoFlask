from setuptools import setup

setup(
    name="legalTechFlask",
    packages=[
        "legalTechFlask"
    ],
    include_package_data=True,
    install_requires=[
        "flask",
        "moviepy",
    ],
)
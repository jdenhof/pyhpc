from setuptools import find_packages, setup

setup(
    name="pyhpc",
    description="HPC Python Helper",
    version="0.0.1.dev1",
    url="https://github.com/jdenhof/pygit",
    author="Jagger Denhof",
    packages=find_packages(),
    install_requires=[
        'paramiko'
    ],
    # extras_require={
    #     "test": [
    #         "pytest",
    #         "pytest-cov"
    #     ]
    # }
)

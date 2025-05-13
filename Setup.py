from setuptools import setup, find_packages

setup(
    name="toc-automata-package-a23",
    version="0.1.0",
    author="Ahmed Adel",
    description="A package to solve automata problems",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    extras_require={
        "dev": ["pytest>=7.0"],
    },
)
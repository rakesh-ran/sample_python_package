from setuptools import setup, find_packages

setup(
    name="sample_python_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author="Your Name",
    author_email="your_email@example.com",
    description="A sample Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/your_username/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

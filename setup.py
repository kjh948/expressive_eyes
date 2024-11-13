import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="expressive-eyes-improved",
    version="0.0.1",
    author="Bahadir Batuhan Kaya, Séverin Lemaignan",
    author_email="severin.lemaignan@brl.ac.uk",
    description="Procedural, interactive expressive eyes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir = {'': 'src'},
    packages=['expressive_eyes'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

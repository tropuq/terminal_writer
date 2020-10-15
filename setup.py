import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terminal_writer_tropuq",
    version="0.0.2",
    author="Michał Niciejewski",
    author_email="quport@gmail.com",
    description="A library allowing multi-terminal scripting and creating scripts for applications with command-line interfaces. Allows to create easy ad-hoc scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tropuq/terminal_writer",
    packages=setuptools.find_packages(),
    scripts=["bin/main.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)

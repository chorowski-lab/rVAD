import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rvadfast",
    version="2.0",
    description="Small packaging of rVAD-fast codebase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chorowski-lab/rVAD",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['scipy', 'numpy'],
    scripts=['scripts/rVAD_fast.py']
)

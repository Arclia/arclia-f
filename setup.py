import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="arclia-f",
  version="0.0.1",
  description="Typesafe higher-order functions",
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=setuptools.find_namespace_packages(
    include=["arclia.*"],
  ),
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.10',
)

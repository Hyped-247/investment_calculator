import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name="investment_calculator",
	version="0.0.1",
	author="Mohammad Mahjoub",
	author_email="myeamil@gmail.com",
	description="Here is my python code does.",
	long_description=long_description,
	url="https://github.com/Hyped-247/investment_calculator.git",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	]
)






















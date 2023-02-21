from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
		name = 'udemy',
		version = '0.1.2',		
		author = 'Szabó Dániel Ernő',
		author_email = 'r3ap3rpy@gmail.com',
		description = 'Python library for interacting with the udemy API 2.0!',
		long_description = 'Python library for interacting with the udemy API 2.0!',
		url="https://github.com/r3ap3rpy/udemy",
		license = 'MIT',
		packages = ['udemy'],
		zip_safe = False,
		include_package_data=True,
		install_requires=['requests'],
      	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	)

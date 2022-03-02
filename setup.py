import pathlib

from setuptools import setup, find_packages

path = pathlib.Path(__file__).parent
README = (path / "README.md").read_text()
setup(
    name='emaileasy',
    version='1.0.2',
    description='A python email sender library',
    long_description_content_type="text/markdown",
    long_description=README,
    author='Erastus Nzula',
    author_email='nzulaerastus@gmail.com',
    url='https://github.com/erastusnzula/easy-email',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(exclude=('tests',)),
    py_modules=['emaileasy'],
    include_package_data=True,
    python_requires='>=3.8',
)

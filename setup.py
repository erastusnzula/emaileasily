import pathlib

from setuptools import setup, find_packages

path = pathlib.Path(__file__).parent
README = (path / "README.md").read_text()
setup(
    name='emaileasy',
    version='1.0.0',
    description='A quick way to send emails.',
    long_description=README,
    author='Erastus',
    author_email='nzulaerastus@gmail.com',
    url='',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    py_modules=['emaileasy'],
)

import pathlib

from setuptools import setup, find_packages

path = pathlib.Path(__file__).parent
README = (path / "README.md").read_text()
setup(
    name='emaileasily',
    version='0.1.4',
    author='Erastus Nzula',
    author_email='nzulaerastus@gmail.com',
    description='A python email library to send and read emails.',
    long_description_content_type="text/markdown",
    long_description=README,
    url='https://github.com/erastusnzula/easy-email',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(exclude=('tests',)),
    install_requires=[],
    include_package_data=True,
    python_requires='>=3.6',
)

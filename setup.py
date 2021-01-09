from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_desc = (here / 'README.md').read_text(encoding='utf-8')


setup(
        name='pycra',
        version='0.0.1',
        description='Python tool to create an react web app for django or flask backend',
        long_description=long_desc,
        long_description_content_type='text/markdown',
        url='https://github.com/Moaz-Mohammed-Elesawey/py-cra',
        author='Moaz Mohammed El-Esawey',
        author_email='mohammedmiaz3141@gmail.com',
        classifiers=[
            'Licence :: OSI Approved :: MIT Licence',
            'Programming Language :: Python :: 3',
        ],
        keywords='react, frontend, python, pycra',
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        python_requires='>=3.6, <4',
)

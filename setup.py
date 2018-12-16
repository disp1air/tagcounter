from setuptools import setup

setup(
    name='tagcounter',
    version='1.0',
    author='Authorrr',
    py_modules=['tagcounter', 'read_write', 'data', 'tagcount', 'const', 'config', 'check_synonyms', 'gui'],
    description='Description',
    include_package_data=True,
    entry_points={'console_scripts': ['tagcounter = tagcounter:main']},
)

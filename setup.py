from setuptools import setup

setup(
    name = 'cf_cli',
    version = '1.0',
    author = 'Shubham Ivane', 
    py_modules = ['cf'],
    install_requires = [
        'Click',
        'requests',
        'beautifulsoup4'
    ],
    entry_points = '''
        [console_scripts]
        cf=cf.main:cli
    ''', 
)

from setuptools import setup, find_packages

setup(
    name='tagcounter',
    version='1.0.1',
    description=u"Tool for count tags by URI",
    long_description=open('README.md').read(),
    author=u"Oleksandr Kubrak",
    author_email='kubrack@gmail.com',
    url='https://github.com/kubrack/tagcounter',
    license='MIT',
    include_package_data=True,
    install_requires=[
        'pyyaml',
    ],
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': ['tagcounter = tagcounter:main'],
    }
)

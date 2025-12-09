from setuptools import setup, find_packages

setup(
    name='apiverve_htmlentitiesencoder/decoder',
    version='1.1.12',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='HTML Entities Encoder/Decoder is a tool for encoding and decoding HTML entities. It converts special characters to HTML entities and vice versa to prevent XSS attacks and display special characters properly.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

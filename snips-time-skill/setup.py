from setuptools import setup

setup(
    name='timelogger',
    version='1.0',
    description='Time skill for Snips',
    author='Snips Labs',
    author_email='labs@snips.ai',
    url='',
    download_url='',
    license='MIT',
    install_requires=['arrow'],
    keywords=['snips'],
    package_data={'timelogger': []},
    packages=['timelogger'],
    include_package_data=True
)

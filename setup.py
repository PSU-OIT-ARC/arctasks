import sys
from setuptools import setup

install_requires = [
    'awscli',
    'packaging>=16.8',
    'runcommands>=1.0a26.dev0',
    'setuptools>=36.2.2',
]

if sys.version_info[:2] < (3, 4):
    install_requires.append('enum34')

setup(
    name='psu.oit.arc.tasks',
    version='1.1.0.dev0',
    author='Wyatt Baldwin',
    author_email='wbaldwin@pdx.edu',
    description='Commands for WDT (formerly ARC) projects',
    license='MIT',
    url='https://github.com/PSU-OIT-ARC/arctasks',
    install_requires=install_requires,
    extras_require={
        'dev': [
            'Sphinx>=1.6.3,<1.7',
            'sphinx_rtd_theme'
        ]
    },
    packages=['arctasks', 'arctasks.aws'],
    package_data={
        'arctasks': [
            'commands.cfg',
            'rsync.excludes',
            'templates/*.template',
        ],
        'arctasks.aws': [
            'commands.cfg',
            'templates/*.template',
            'templates/*.conf',
            'templates/*.ini',
            'templates/cloudformation/*.template.yml',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

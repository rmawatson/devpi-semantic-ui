from setuptools import setup


def _md(filename):
    '''
    Load md file and sanitize it for PyPI.
    Remove unsupported github tags:
     - code-block directive
     - all badges
    '''
    content = open(filename, encoding='utf-8').read()
    return content


long_description = '\n'.join((
    _md('README.md'),
    _md('CHANGELOG.md'),
    ''
))

exec(compile(
    open('devpi_semantic_ui/__about__.py', encoding='utf-8').read(),
    'devpi_semantic_ui/__about__.py',
    'exec'
))

setup(
    name="devpi-semantic-ui-ng",
    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/rmawatson/devpi-semantic-ui",
    version=__version__,
    author="API Hackers",
    author_email="github@apihackers.com",
    maintainer="rmawatson",
    maintainer_email="rmawatson@hotmail.com",
    license="MIT",
    entry_points={
        'devpi_server': [
            "devpi-semantic-ui-ng = devpi_semantic_ui"
        ]
    },
    install_requires=['devpi-web', 'pluggy'],
    python_requires='>=3.9',
    include_package_data=True,
    zip_safe=False,
    packages=['devpi_semantic_ui'],
    keywords='devpi semantic-ui',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ],
)

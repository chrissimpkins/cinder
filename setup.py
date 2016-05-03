from setuptools import setup, find_packages

VERSION = '0.4.0'


setup(
    name="mkdocs-psinder",
    version=VERSION,
    url='https://github.com/michaeltlombardi/mkdocs-psinder',
    license='MIT',
    description='A clean, responsive PowerShell-inspired theme for static documentation websites that are generated with MkDocs - forked with love from Chris Simpkins Cinder',
    author='Michael T Lombardi',
    author_email='michael.t.lombardi@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'psinder = psinder',
        ]
    },
    zip_safe=False
)

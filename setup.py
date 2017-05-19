from setuptools import setup, find_packages

VERSION = '0.9.4'


setup(
    name="mkdocs-cindercone",
    version=VERSION,
    url='https://github.com/scotte/cindercone',
    license='MIT',
    description='A clean responsive theme for the MkDocs static documentation site generator based on cinder',
    author='Christopher Simpkins (cinder), Scott Emmons (cindercone)',
    author_email='scotte@users.noreply.github.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'cindercone = cindercone',
        ]
    },
    zip_safe=False
)

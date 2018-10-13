from setuptools import setup


setup(
    name='Skeleton',
    version='1.0',
    py_modules=['skeleton'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        skeleton=skeleton.cli:main
    '''
)
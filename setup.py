from setuptools import setup, find_packages


setup(
    name='django-pygments',
    version='0.2',
    description=('A django app that provides a template tag and filters for '
                 'enabling syntax highlighting with Pygments'),
    long_description=open('README.rst').read(),
    author='Stefan Talpalaru',
    author_email='developers@od-eon.com',
    url='http://github.com/odeoncg/django-pygments/tree/master',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Pygments'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

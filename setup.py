from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='django-registration-fc',
    version='1.0',
    description='Fork of an extensible user-registration application for Django',
    author='Ilya Baryshev',
    author_email='baryshev@futurecolors.ru',
    url='https://github.com/futurecolors/django-registration',
    package_dir={'registration': 'registration'},
    packages=find_packages(exclude='test_app'),
    install_requires=[
        'django-templated-email==0.4.7',
        'django-braces==1.0.0',
    ],
    tests_require=['pytest-django'],
    cmdclass={'test': PyTest},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
)

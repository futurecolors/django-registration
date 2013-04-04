from setuptools import setup, find_packages


setup(
    name='django-registration',
    version='1.0',
    description='An extensible user-registration application for Django',
    author='James Bennett',
    author_email='james@b-list.org',
    url='http://www.bitbucket.org/ubernostrum/django-registration/wiki/',
    download_url='http://www.bitbucket.org/ubernostrum/django-registration/get/v0.8.gz',
    package_dir={'registration': 'registration'},
    packages=find_packages(exclude='test_app'),
    tests_require=(
        'django-setuptest',
    ),
    test_suite='setuptest.setuptest.SetupTestSuite',
    include_package_data=True,
    classifiers=['Development Status :: 4 - Beta',
               'Environment :: Web Environment',
               'Framework :: Django',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Software Development :: Libraries :: Python Modules',
               'Topic :: Utilities'],
)

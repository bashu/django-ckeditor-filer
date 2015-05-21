import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ckeditor-filer',
    version='0.1',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    license='MIT License',
    description='Django CKEditor Filer',
    long_description=README,
    url='http://github.com/bashu/django-ckeditor-filer',
    author='Basil Shubin',
    author_email='basil.shubin@gmail.com',
    install_requires=[
    ],    
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)


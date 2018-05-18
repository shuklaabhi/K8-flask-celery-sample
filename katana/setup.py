from setuptools import find_packages, setup

setup(
    name='Katana',
    description='K8 Sample application using python stack',
    version='0.2',
    license='BSD',
    platforms=['any'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    tests_require=[
        'codeclimate-test-reporter',
        'coverage',
        'mock',
        'nose',
        'redis',
    ],
    author='Abhishek Shukla',
    author_email='shukla.abhishek02@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent'
    ],
)
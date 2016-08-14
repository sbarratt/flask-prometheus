from setuptools import setup

setup(
    name='Flask-Prometheus',
    version='0.0.1',
    url='http://github.com/sbarratt/flask-prometheus',
    license='BSD',
    author='Shane Barratt',
    author_email='stbarratt@gmail.com',
    maintainer='Shane Barratt',
    maintainer_email='stbarratt@gmail.com',
    description='Prometheus client instrumentation for flask.',
    long_description=__doc__,
    packages=['flask_prometheus'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'prometheus-client>=0.0.14'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',

        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Topic :: System :: Monitoring',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='prometheus monitoring'
)

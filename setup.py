from setuptools import setup

setup(
    name='django_geogebra',
    version='0.0.1',
    packages=['django_geogebra'],
    url='https://github.com/k0t3n/django_geogebra',
    license='MIT',
    author='Alexey Kotenko',
    author_email='alexey@kotenko.me',
    description='Geogebra integration for Django',
    install_requires=[
        'django>=3.0'
    ],
    python_requires='>=3',
)

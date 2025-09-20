from setuptools import setup, find_packages

setup(
    name='exoplanet_explorer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas>=2.0',
        'plotly>=6.0',
        'requests>=2.30',
        'numpy>=1.25'
    ],
    author='Your Name',
    description='Python library to explore NASA Exoplanet Archive data with visualization and analysis.',
    url='https://github.com/notsajeed/exoplanet_explorer',
    python_requires='>=3.10',
)

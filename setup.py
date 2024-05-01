# setup.py
from setuptools import setup, find_packages

setup(
    name='filechat',
    version='1.0.0',
    author='Danny Liu',
    author_email='dannyjialiliu@gmail.com',
    description='A CLI tool for generating and executing MacOS commands using the Ollama API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dannyl1u/filechat',
    packages=find_packages(),
    install_requires=[
        'ollama',
    ],
    entry_points={
        'console_scripts': [
            'filechat=filechat.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='cherrant',
    version='0.0.1',
    author='Yue Zhang',
    author_email='hillzhang1999@qq.com',
    license='MIT',
    description='A Chinese GEC evaluation tool',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Jacob-Zhou/ChERRANT',
    packages=find_packages(),
    package_data={
        'cherrant': ['data/*.txt'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic'
    ],
    setup_requires=[
        'setuptools',
    ],
    install_requires=[
        'ltp==4.1.3.post1',
        'torch<2.0.0',
        'OpenCC>=1.1.2,<=1.1.6',
        'python-Levenshtein==0.12.1',
        'pypinyin',
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'parallel-to-m2=cherrant.parallel_to_m2:main',
            'compare-m2=cherrant.compare_m2_for_evaluation:main',
            'rule-ensemble=cherrant.rule_ensemble:main',
            'm2-convertor=cherrant.m2convertor:main',
        ]
    },
    python_requires='>=3.7',
    zip_safe=False
)
#!/usr/bin/env python
import setuptools
import codecs

long_description = codecs.open('README.rst', 'r', 'utf-8').read()

setuptools.setup(
      name='treeutils',
      version='0.1.1',
      description=('For developers who have to fit real world data into '
                   'tree structures like the D3 tree.'), 
      long_description=long_description,
      author='Charles Kaminski',
      author_email='CharlesKaminski@gmail.com',
      url='https://github.com/Charles-Kaminski/treeutils',
      keywords = ['Tree', 'Cluster', 'Parent', 'Child', 'Branch', 'Root', 'D3'],
      license='BSD 3-Clause License',
      py_modules=['treeutils.__init__',],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Sociology',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Utilities',
      ] 
)

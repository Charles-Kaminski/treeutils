treeutils
=========================

For developers who have to fit real world data into tree structures like the D3 tree.

Separate records into different trees.  Build child trees from a parent relationship.  Order does not matter.  Having more than one tree present does not matter.  Broken branches do not matter.

:Download: http://pypi.python.org/pypi/treeutils/
:Source: http://github.com/Charles-Kaminski/treeutils
:License: BSD 3-Clause License

Usage
=====

**Commands**::

    >> clusters = [x for x in Clusters(records)]
    >> clusters = list(Clusters(records))
    >> trees = [x for x in Trees(records)]
    >> trees = list(Trees(records))
    
Use Clusters when you don't want to build trees but instead you want to return the records grouped by tree membership.  Clusters takes an unordered list of dictionary objects with an ID and a Parent ID. Clusters will separate them into separate lists based on tree membership.

Use Trees when you want to build out trees and you have an unordered list of records with parent relationships instead of child relationships and you may have more than one tree present.  Clusters takes an unordered list of dictionary objects with an ID and a Parent ID. Trees will build out the trees by embedding child nodes into each parent's children key.  Trees will return the root node of each separate tree.

Installing treeutils
====================================

You can install ``treeutils`` either via the Python Package Index (PyPI) or from source.

To install using ``pip`` (recommended)::

    $ pip install treeutils

To install using ``easy_install``::

    $ easy_install treeutils


To install from source, download the source from github (http://github.com/Charles-Kaminski/treeutils/downloads).  Decompress it and put it in the folder with your python project as another python module.
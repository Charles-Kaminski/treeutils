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

Method
======

For each template, the minimizer command:  

1. Replaces any ``{# NOMINIFY #} {# ENDNOMINIFY #}`` tags and content with a unique identifier and saves the content in memory so that it is excluded from the rest of the process.

2. Remaining Django comments are removed.

3. Django tags and django variables are replaced with unique identifiers.  The tags and variables are saved in memory.  This approach "protects" the tags and variables from the minimizers.  It also allows you to use Django tags and variables inside your javascript and CSS without ill effect by the CSS or javascript minimizer.

4. HTML script tags and content are replaced with unique identifiers. The tags and content are saved in memory for additional processing.  The type attribute for the script tag is checked to see if the script content is javascript.  If no type is provided, then javascript is assumed.  Any javascript is then run through the javascript minimizers.

5. An almost identical process to step 4 is implemented on the HTML style tags for css.

6. The remaining text (with the identifiers) is run through the html minimizers.

7. All of the content saved in memory and associated with unique identifiers are put back.

8. The original template is moved to an archive folder.  The minimized template is put in the original location.
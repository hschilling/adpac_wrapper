

#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Scott E. Townsend',
 'author_email': 'scott.e.townsend@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'Component wrapper for ADPAC (Advanced Ducted Propfan Analysis Code)',
 'download_url': '',
 'entry_points': '[openmdao.component]\nadpac_wrapper.adspin.ADSPIN=adpac_wrapper.adspin:ADSPIN\nadpac_wrapper.wrapper.ADPAC=adpac_wrapper.wrapper:ADPAC',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Scott E. Townsend',
 'maintainer_email': 'scott.e.townsend@nasa.gov',
 'name': 'adpac_wrapper',
 'package_data': {'adpac_wrapper': ['sphinx_build/html/usage.html',
                                    'sphinx_build/html/py-modindex.html',
                                    'sphinx_build/html/genindex.html',
                                    'sphinx_build/html/search.html',
                                    'sphinx_build/html/srcdocs.html',
                                    'sphinx_build/html/index.html',
                                    'sphinx_build/html/objects.inv',
                                    'sphinx_build/html/searchindex.js',
                                    'sphinx_build/html/.buildinfo',
                                    'sphinx_build/html/pkgdocs.html',
                                    'sphinx_build/html/_sources/pkgdocs.txt',
                                    'sphinx_build/html/_sources/srcdocs.txt',
                                    'sphinx_build/html/_sources/index.txt',
                                    'sphinx_build/html/_sources/usage.txt',
                                    'sphinx_build/html/_modules/index.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/restart.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/boundata.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/inleta.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/lamss.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/fixed.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/vis3d.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/system.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/wrapper.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/local_units.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/free.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/inletg.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/adspin.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/kill.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/inletm.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/endtta.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/property.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/bcint1.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/bcintm.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/bcprr.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/bc.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/bdatin.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/converge.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/inlett.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/mbcavg.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/vce.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/input.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/ssvi.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/exitg.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/bcprm.html',
                                    'sphinx_build/html/_modules/adpac_wrapper/inletr.html',
                                    'sphinx_build/html/_static/underscore.js',
                                    'sphinx_build/html/_static/pygments.css',
                                    'sphinx_build/html/_static/basic.css',
                                    'sphinx_build/html/_static/file.png',
                                    'sphinx_build/html/_static/sidebar.js',
                                    'sphinx_build/html/_static/jquery.js',
                                    'sphinx_build/html/_static/default.css',
                                    'sphinx_build/html/_static/minus.png',
                                    'sphinx_build/html/_static/doctools.js',
                                    'sphinx_build/html/_static/searchtools.js',
                                    'sphinx_build/html/_static/plus.png',
                                    'test/test_wrapper.py',
                                    'test/__init__.py',
                                    'test/all-bcs.boundata',
                                    'test/test_input.py',
                                    'test/all-bcs.input']},
 'package_dir': {'': 'src'},
 'packages': ['adpac_wrapper', 'adpac_wrapper.test'],
 'url': 'https://github.com/OpenMDAO-Plugins/adpac_wrapper',
 'version': '0.3',
 'zip_safe': False}


setup(**kwargs)


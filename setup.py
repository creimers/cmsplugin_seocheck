try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cmsplugin_seocheck

version = cmsplugin_seocheck.__version__

setup(
    name = 'cmsplugin_seocheck',
    packages = ['cmsplugin_seocheck'],
    include_package_data = True,
    version = version,
    description = "A djangocms plugin to check your page's SEO properties",
    author = 'Christoph Reimers',
    author_email = 'christoph@superservice-international.com',
    license='BSD License',
    url = 'https://github.com/creimers/cmsplugin_seocheck',
    keywords = ['djangocms', 'django', 'SEO',], 
    install_requires = ['django-cms>=3.0',],
    classifiers = [
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)

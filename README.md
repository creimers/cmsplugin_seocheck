[![Latest Version](https://pypip.in/version/cmsplugin_seocheck/badge.svg)](https://pypi.python.org/pypi/cmsplugin-seocheck/)
[![Supported Python versions](https://pypip.in/py_versions/cmsplugin_seocheck/badge.svg)](https://pypi.python.org/pypi/cmsplugin-seocheck/)
[![Development Status](https://pypip.in/status/cmsplugin_seocheck/badge.svg)](https://pypi.python.org/pypi/cmsplugin_seocheck/)
# djangocms SEO check plugin

A djangocms plugin to check SEO aspects of your page.

## Installation

* ``pip install cmsplugin_seocheck``

* add ``cmsplugin_seocheck`` to ``INSTALLED_APPS`` in ``settings.py``

* add ``url(r'^originalseourl/', include('cmsplugin_seocheck.urls', namespace="cmsplugin_seocheck")),`` to ``myproject/urls.py``

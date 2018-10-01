# don't try this at home!

[![Build Status](https://travis-ci.org/creimers/cmsplugin_seocheck.svg?branch=master)](https://travis-ci.org/creimers/cmsplugin_seocheck)
[![Coverage Status](https://coveralls.io/repos/creimers/cmsplugin_seocheck/badge.svg?branch=develop)](https://coveralls.io/r/creimers/cmsplugin_seocheck?branch=develop)
[![Code Climate](https://codeclimate.com/github/creimers/cmsplugin_seocheck/badges/gpa.svg)](https://codeclimate.com/github/creimers/cmsplugin_seocheck)
[![Requirements Status](https://requires.io/github/creimers/cmsplugin_seocheck/requirements.svg?branch=master)](https://requires.io/github/creimers/cmsplugin_seocheck/requirements/?branch=master)
[![Latest Version](https://pypip.in/version/cmsplugin_seocheck/badge.svg)](https://pypi.python.org/pypi/cmsplugin-seocheck/)
[![Supported Python versions](https://pypip.in/py_versions/cmsplugin_seocheck/badge.svg)](https://pypi.python.org/pypi/cmsplugin-seocheck/)
[![Development Status](https://pypip.in/status/cmsplugin_seocheck/badge.svg)](https://pypi.python.org/pypi/cmsplugin_seocheck/)
# djangocms SEO check plugin

A djangocms plugin to check SEO aspects of your page. Inspired by [yoast](https://yoast.com/) for wordpress.

This app is far from perfect / complete.

## Installation

* ``pip install --pre cmsplugin_seocheck``

* add ``'cmsplugin_seocheck'`` to ``INSTALLED_APPS`` in ``settings.py``

* add ``url(r'^originalseourl/', include('cmsplugin_seocheck.urls', namespace="cmsplugin_seocheck")),`` to ``myproject/urls.py`` (before the cms' urls).

## Example

![preview](example.png)

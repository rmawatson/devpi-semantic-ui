Changelog
=========

0.3.1 (2026-08-04)
------------------

- Replace deprecated `pkg_resources` with `importlib.resources`, silencing the removal warning on startup
- Declare `python_requires >= 3.9` and build a Python 3 only wheel

0.3.0 (2026-08-04)
------------------

- Theme the user/organisation page (`/{user}`), which previously fell back to the default devpi-web template
- Link organisation names on the home page to their organisation page
- Fix stray characters rendered on the home page

0.2.2 (2017-02-15)
------------------

- Fix navbar width

0.2.1 (2017-02-15)
------------------

- Added syntax highlighting ([#1](https://github.com/apihackers/devpi-semantic-ui/pull/1))
- Upgraded to latest Semantic-UI (2.2.7)
- Handle tox results
- Handle documentation
- Fix sticky footer

0.1.0 (2016-06-07)
------------------

- Initial release

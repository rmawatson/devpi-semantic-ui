Changelog
=========

0.3.3 (2026-10-22)
------------------

- Mark the theme's devpi-server hooks with devpi-server's pluggy `HookimplMarker`: pluggy registers only marked hooks, so they were never called
- `--theme semantic-ui` now works: it was taken as a path, and devpi-server exited (passing the package's directory as `--theme` worked)
- The search box shows live results: the JSON search view they come from was never added, so the box showed nothing until a search was submitted
- The JSON search view is added after devpi-web's search page, and takes only requests with a JSON `Content-Type`, so a browser's request for `/+search` always gets the page
- The JSON search view is now added whenever the package is installed, with or without `--theme`
- The JSON search returns its query as a string, and the "View all" link URL-encodes it
- Declare `pluggy`, which the package now imports
- Read the README and the changelog as UTF-8 when building, whatever the build machine's locale

0.3.2 (2026-08-04)
------------------

- Republished as `devpi-semantic-ui-ng`, a maintained fork of `devpi-semantic-ui` (unreleased since 0.2.2 in 2017). The import package and the `--theme semantic-ui` option are unchanged
- Fix `KeyError` on tox results that carry no `failed` key ([#11](https://github.com/apihackers/devpi-semantic-ui/pull/11), thanks con-f-use)
- Take the live search URL from the search form's action instead of a hardcoded `/+search`, so the dropdown works when devpi is served under a URL prefix ([#8](https://github.com/apihackers/devpi-semantic-ui/pull/8), thanks tobyX)

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

import os

from importlib.resources import files

from pluggy import HookimplMarker

from .__about__ import __version__, __description__


# devpi-server loads its plugins with pluggy, which registers only the
# functions marked for its project. Unmarked, the hooks below were never
# called: `--theme semantic-ui` was taken as a path and devpi-server exited,
# and the JSON search view the search box uses was never added.
hookimpl = HookimplMarker("devpiserver")


@hookimpl
def devpiserver_cmdline_run(xom):
    '''
    Load theme when `theme` parameter is 'semantic-ui'.
    '''
    if xom.config.args.theme == 'semantic-ui':
        xom.config.args.theme = os.fspath(files('devpi_semantic_ui'))
        xom.log.info("Semantic UI Theme loaded")


# Last, after devpi-web's: its HTML search route on /+search is then tried
# before this package's JSON one.
@hookimpl(trylast=True)
def devpiserver_pyramid_configure(config, pyramid_config):
    '''Perform Pyramid level configuration'''
    pyramid_config.include('devpi_semantic_ui')


def includeme(config):
    # Only the search box's own requests, which send a JSON Content-Type.
    # A route matched on Accept alone would also take a browser's (whose
    # Accept includes */*) if it came first, and its view, which needs that
    # Content-Type, would then answer 404 instead of devpi-web's page.
    config.add_route('searchapi', '/+search', accept='application/json',
                     header='Content-Type:application/json')
    config.scan()

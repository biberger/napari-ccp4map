# napari-ccp4map

[![License](https://img.shields.io/pypi/l/napari-ccp4map.svg?color=green)](https://github.com/biberger/napari-ccp4map/raw/master/LICENSE)
[![DOI](https://zenodo.org/badge/413461420.svg)](https://zenodo.org/badge/latestdoi/413461420)
[![PyPI](https://img.shields.io/pypi/v/napari-ccp4map.svg?color=green)](https://pypi.org/project/napari-ccp4map)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-ccp4map.svg?color=green)](https://python.org)
[![tests](https://github.com/biberger/napari-ccp4map/workflows/tests/badge.svg)](https://github.com/biberger/napari-ccp4map/actions)
[![codecov](https://codecov.io/gh/biberger/napari-ccp4map/branch/master/graph/badge.svg)](https://codecov.io/gh/biberger/napari-ccp4map)

Enables napari to read .map files in the ccp4 format.

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation

You can install `napari-ccp4map` via [pip]:

    pip install napari-ccp4map

## Usage
If the plugin was installed correctly, it will pop up in a napari window under Plugins->Install/Uninstall Plugins.
You can either drag&drop filed into the window to read them, or search for a folder/file using Ctrl+O.

## How it works
This plugin simply reads a file and allows [gemmi](https://github.com/project-gemmi/gemmi) to interact with it. Then, numpy turns the file into an array.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-ccp4map" is free and open source software

## Citing napari-ccp4map
If you find napari-ccp4map useful please cite this repository using its DOI as follows:

    Simon Biberger (2021). napari-ccp4map: a napari plugin to read ccp4 .map files. doi:10.5281/zenodo.3555620

Note this DOI will resolve to all versions of napari-ccp4map. To cite a specific version please find the DOI of that version on our zenodo page. The DOI of the latest version is in the badge at the top of this page.

You can also use the BibTeX below:
```
@software{napari-ccp4map,
  author = {Simon Biberger},
  title = {Napari-ccp4map},
  url = {https://github.com/biberger/napari-ccp4map},
  version = {1.1},
  doi = {10.5281/zenodo.3555620},
  date = {2021-10-05},
}
```
If these remarks on citations seem a bit excessive, then you are probably right. I am using this as my test case for another library ([Cestimii](https://github.com/biberger/cestimii)).

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/biberger/napari-ccp4map/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

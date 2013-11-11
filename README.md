RobotFramework-Plus Tool Collection
====================

This is a Collection of RobotFramework tools, functionality not yet
provided by the RobotFramework test-framework (2.8.1).

The features are:

- Embedding charts into the test-reports, for example to illustrate
  performance measurements etc.

- Extended process management functionality.

The Chart-tool generates SVG diagrams and embeds them into the
test-report wihtout external files or references.

## Requirenments

The tool collection extends RobotFramework 2.8.1 and in addition
requires the svg.charts Python-library and must be available on the
machine. The following command must be executed to install svg.charts
with root permission:

```
sudo pip install robotframework svg.charts robotframeworkplus
```

The environment variable PYTHONPATH should point to the directory
where the tool colleciton is located, for example

```
export PYTHONPATH=$HOME/robotframeworkplus/lib
```

Executing the demo-tests:

```
PYTHONPATH=$HOME/robotframeworkplus/lib pybot $HOME/robotframework_tools/demo
```

The bar-chart will be embedded into the report.html file and can be
viewed by web-browser (see [docs/screenshot-chart.png](docs/screenshot-chart.png)), 


## Compatibility

- Python 2.7.3 (or later)
- RobotFramework 2.8.1 (or later)
- Python SVG Charting Library svg.charts 2.2 (or later)

## Usage

Please see the demo.

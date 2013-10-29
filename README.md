
RobotFramwork Tool Collection
====================

This is a Collection of RobotFramework tools, functionality not yet provided by the RobotFramework test-framework (2.8.1). 

The features are:
- Embedding charts into the test-reports, for example to illustrate performance measurements etc.
- Extended process management functionality.

for the python svg.charts library.  Measured values can be converted into SVG diagrams,
being embedded into the testsuite report (no external file).

## Requirenments

The tool collection extends RobotFramework 2.8.1 and in addition requires the svg.charts Python-library and must be available on the machine. The following command must be executed  to install svg.charts with root permission:

```
sudo pip install svg.charts
```

The environment variable PYTHONPATH should point to the directory where the tool colleciton is located, for example

```
export PYTHONPATH=$HOME/robotframework_tools/lib
```

## Compatibility

- Python 2.7.3 (or later)
- RobotFramework 2.8.1 (or later)
- Python SVG Charting Library svg.charts 2.1 (or later)

## Usage

Please see the demo.

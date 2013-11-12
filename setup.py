#  Copyright 2013 Frehberg IT <frehberg@gmail.com>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read()

setup(
    name = "robotframeworkplus",
    version = "0.2",  
    py_modules = ['lib/RobotChart', 'lib/RobotProcessEx'],
    setup_requires = ["svg.charts >= 2.2", "robotframework" ],
    author = "Frank Rehberger",
    author_email = "frehberg@gmail.com",
    description = "This is a Toolset adding new functionalities to  RobotFramework, such as embedding chart diagrams or improved process management",
    license = "Apache License",
    url = "https://github.com/frehberg/robotframeworkplus",
    long_description=long_description)

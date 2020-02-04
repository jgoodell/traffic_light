# Introduction

A traffic light simulator with an ASCII interface.

## Installation & Setup

The package is installable for development with
``` shell
$ python setup.py develop
```
from the projects root directory. Of for production with
``` shell
$ python setup.py install
```

## Usage

The application can be started with
``` shell
$ python traffic_light.py -H 20 -c 5 -p 30
```
from the commandline after the package has been installed either for develpment or production.
The '-H' argument is for the 'halt' duration, or how long the light will be red. The '-c'
argument is for the 'caution' duration, or how long the light will be yellow. The '-p' argument
is the 'proceed' duration, or how long the light will be green.

Once the simulator has started, you will be greated with the interactive command line. Type and
enter 'start' to launch thetraffic light simulator.
``` shell
(Cmd) start
```

You can exit the application at anytime with ctrl-C which will start the graceful shut down
sequence, or with ctrl-C again to immediately shut down the traffic light simulator.
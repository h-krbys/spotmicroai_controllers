# spotmicroai_controllers

## Package List

| Package | Detail |
| --- | --- |
| spot_description | urdf model of spotmicroai |
| spot_driver      | hardware managemant |
| spot_interface   | control interface |
| spot_planner     | motion planner (mainly walk) |

## Dependency

This package depends on following packages.

| Package | Detail |
| --- | --- |
| champ |Open source development framework for building new quadrupedal robots and developing new control algorithms.|
<!--
| towr  |Light-weight and extensible C++ library for trajectory optimization for legged robots.|
| ifopt |Eigen-based, light-weight C++ Interface to NLP Solvers (Ipopt, Snopt).|
| xpp   |Visualization of legged robots, forces, support areas, ZMP, CoM etc. in ROS rviz.|
-->


Please install necessary packages.

```
$ sudo apt install -y python-rosdep

$ cd ~/catkin_ws/src
$ git clone https://github.com/chvmp/champ
$ git clone https://github.com/chvmp/champ_teleop
$ cd ..
$ rosdep install --from-paths src --ignore-src -r -y
```
<!--
```
$ sudo apt install ros-melodic-towr-ros
$ sudo apt install ros-melodic-ifopt
$ sudo apt install ros-melodic-xpp
```
-->

sudo apt-get install ros-melodic-joy

### clone

```
$ cd Downloads
$ git clone https://github.com/TeraHz/I2C
$ git clone https://github.com/TeraHz/PCA9685
```

### Catkin Config

```
$ catkin config --cmake-args -DI2C_DIR=~/Downloads/I2C -DPCA9685_DIR=~/Downloads/PCA9685
```

## Joycon

### Joystick Name
Sony DualShock3

### Intstallation

site: https://askubuntu.com/questions/913599/how-to-connect-dualshock-3-controller-ps3-sixaxis-gamepad-on-ubuntu-16-04

```
$ sudo apt-get install dialog build-essential pyqt4-dev-tools libusb-dev libbluetooth-dev python-dbus -y
$ cd Downloads
$ wget https://github.com/RetroPie/sixad/archive/master.zip -O sixad-master.zip
$ unzip sixad-master.zip
$ cd sixad-master
$ make
$ sudo make install
```

### Usage

Plug in the controller via USB first to do the initial pairing. Run the sixpair command:

```
$ sudo sixpair
```

Unplug the controller and run:

```
$ sudo sixad -s
```
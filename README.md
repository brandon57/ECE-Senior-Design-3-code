
# ECE-Senior-Design-3-code

[Parts List](https://ndusbpos-my.sharepoint.com/:x:/g/personal/brandon_sitarz_ndus_edu/EYj7pP6WB-dNunrzTcp5bb8Bgdo8WEn6w1ga-DmnN949Dw?e=9menLp)

## Installation and Dependencies:
The following instructions are based on Debian Linux:

First, update and upgrade all apt packages

    sudo apt update && sudo apt upgrade -Y

After cloning the repository, install python3.

    sudo apt install python3

Also install python3-venv

    sudo apt install python3-venv

Make sure your current working directory is in the repository directory, example..

    cd ECE-Senior-Design-3-code

Now lets create a virtual environment

    python3 -m venv sd3

To activate the virtual environment

    source sd3/bin/activate

Install the following python3 packages:

    pip install tkintermapview
    pip install pyserial
    pip install smbus2

## Running the program
Open a terminal in the directory of the application.

If not already, activate the venv:

    source sd3/bin/activate

And run the program with python3:

    python3 main.py



# ECE-Senior-Design-3-code

[Parts List](https://ndusbpos-my.sharepoint.com/:x:/g/personal/brandon_sitarz_ndus_edu/EYj7pP6WB-dNunrzTcp5bb8Bgdo8WEn6w1ga-DmnN949Dw?e=9menLp)

## Installation and Dependencies:
Clone the repository and open a terminal within the directory.

Our application uses [poetry](https://github.com/python-poetry/poetry) to manage python dependiences and environment. On a debian linux machine (raspberry pi), run the following to [install it](https://python-poetry.org/docs/#installing-with-pipx).

First update and upgrade your system packages, then install pipx. Copy the below command and run in the terminal:
    sudo apt update && sudo apt upgrade -y && sudo apt install pipx -y && pipx ensurepath

Please reopen your terminal and navigate to the cloned repository.

Now you can install poetry:
    pipx install poetry

Set up poetry for our app by typing:
    poetry install

You may be prompted to set up a keyring (raspberry pi), this sometimes causes the install to hang, if after 5 minutes you see no progress, use Ctrl+C to cancel the install and run the command again.

You have now completed the setup! You may need to install python3 on your system if it is not already there.

## Running the program
Open a terminal in the project directory
Run:
    poetry run python main.py
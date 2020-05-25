#! /bin/sh

echo "Installing Homebrew"

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" && echo "Homebrew has been installed" || echo "Failed to install Homebrew"

brew install python && echo "python had been installed. Checking version" || echo "Error installing python"

python --version

echo "Installing pip for required python libraries"

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py && echo "pip successfully installed, checking version" || echo "error installing pip"

pip --version

pip install numpy pandas






`sudo apt update`{{execute}}

`sudo apt-get install python3.6 python3.6-dev`{{execute}}

install 
    5  apt-get install python3.6-dev
    6  apt-get install libatlas-base-dev
    7  apt-get install gfortran
    8  apt-get install pkg-config
    9  
   10  apt-get install libfreetype6

`pip install virtualenv`{{execute}}

`virtualenv --version`{{execute}}

`mkdir virtualenvs`{{execute}}

`cd virtualenvs`{{execute}}

`virtualenv -p python3.6 zipline36`{{execute}}

`mkdir ~/zipline`{{execute}}

`cd ~/zipline`{{execute}}

`. ../virtualenvs/zipline36/bin/activate`{{execute}}

`python --version`{{execute}}

`python3 -V`{{execute}}

`git clone https://github.com/quantopian/zipline.git`{{execute}}

`pip3 install numpy cython matplotlib`{{execute}}

`pip3 install -U setuptools`{{execute}}

`pip3 install zipline`{{execute}}

`zipline --help`{{execute}}

`zipline ingest -b quantopian-quandl`{{execute}}


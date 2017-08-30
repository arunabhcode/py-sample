Setup coding style
==================

**For Linux: Using Sublime 3 as code editor**

- Install prerequisites

~~~~~~~~~~~~~~~~~~~~~
    sudo apt-get install python3 
~~~~~~~~~~~~~~~~~~~~~

- Open Sublime

- Ctrl + `

- copy command from https://packagecontrol.io/installation

- press enter and restart Sublime

~~~~~~~~~~~~~~~~~~~~~
    sudo apt-get install python3-pip 

    sudo pip3 install -r requirements.txt
~~~~~~~~~~~~~~~~~~~~~

- Open Sublime

- ctrl + shift + p

- select "package control: install package"

- search and install SublimeLinter

- search and install SublimeLinter-flake8

- search and install Docblockr_Python

- search and install FileHeader

- search and install PyYapf Python Formatter

- search and install Markdown Preview

- search and install GitGutter

<br />

External Libraries
==================

OpenCV
------

**For Linux**

- Install prerequisites

~~~~~~~~~~~~~~~~~~~~~
    sudo apt-get install cmake libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

    sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
~~~~~~~~~~~~~~~~~~~~~

- Get the latest OpenCV

~~~~~~~~~~~~~~~~~~~~~
    git clone https://github.com/Itseez/opencv

    cd opencv && mkdir build && cd build

    ccmake ..
~~~~~~~~~~~~~~~~~~~~~

- Add/Remove modules accordingly

~~~~~~~~~~~~~~~~~~~~~
    make -j

    sudo make install
~~~~~~~~~~~~~~~~~~~~~

Tensorflow
--------------

**For Linux**

~~~~~~~~~~~~~~~~~
    export tfBinaryURL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.2.1-cp35-cp35m-linux_x86_64.whl
    sudo pip3 install --upgrade tfBinaryURL
~~~~~~~~~~~~~~~~~

 Keras
--------------
     
**For Linux**

~~~~~~~~~~~~~~~~~
    sudo pip3 install keras
~~~~~~~~~~~~~~~~~

Scikit-Learn
--------------

**For Linux**

~~~~~~~~~~~~~~~~~
    sudo pip3 install -U scikit-learn
~~~~~~~~~~~~~~~~~

Matplotlib
-------------

**For Linux**

~~~~~~~~~~~~~~~~~
    sudo pip3 install matplotlib
~~~~~~~~~~~~~~~~~

Jupyter
--------------

**For Linux**

~~~~~~~~~~~~~~~~~
    sudo pip3 install jupyter
~~~~~~~~~~~~~~~~~

Numpydoc
--------

**For Linux**

~~~~~~~~~~~~~~~~~
    sudo easy_install numpydoc
~~~~~~~~~~~~~~~~~


<br />

IDE for debugging and execution
===============================

**For Linux**

~~~~~~~~~~~~~~~~~
    sudo pip3 install spyder
~~~~~~~~~~~~~~~~~


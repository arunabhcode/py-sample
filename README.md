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

    sudo pip install -r requirements.txt
~~~~~~~~~~~~~~~~~~~~~

- Open Sublime

- ctrl + shift + p

- select "package control: install package"

- search and install SublimeLinter

- search and install SublimeLinter-pylint

- search and install AutoDocString

- search and install FileHeader

- search and install PyYapf Python Formatter, change settings

~~~~~~~~~~~~~~~~~~~~~
{
    "on_save": true
}
~~~~~~~~~~~~~~~~~~~~~

- search and install Markdown Preview

<br />

Documentation
=============

- To setup the docs folder use

~~~~~~~~~~~~~~~~~~~~~
sphinx-quickstart
~~~~~~~~~~~~~~~~~~~~~

- To process code documentation into .rst files

~~~~~~~~~~~~~~~~~~~~~
cd docs/
sphinx-apidoc -f -o ./ ../modules/
~~~~~~~~~~~~~~~~~~~~~

- To generate documentation

~~~~~~~~~~~~~~~~~~~~~
cd docs/
make html
~~~~~~~~~~~~~~~~~~~~~

Test
====

- Run tests from root

~~~~~~~~~~~~~~~~~~~~~
pytest -v unit-tests/
~~~~~~~~~~~~~~~~~~~~~

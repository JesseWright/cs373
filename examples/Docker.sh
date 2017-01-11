% which docker
/usr/local/bin/docker



% docker --version
Docker version 1.12.0, build 8eab29e



% docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE



% cat Dockerfile
FROM python:3.5.2

RUN pip install --upgrade pip && \
    pip --version             && \
    pip install coverage      && \
    pip install numpy         && \
    pip install pylint

CMD bash



% docker build -t gpdowning/python .
...



% docker push gpdowning/python
...



% docker pull gpdowning/python
...



% docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
gpdowning/python    latest              9e0a05a1bd40        7 days ago          783.1 MB
python              3.5.2               58528474c16a        2 weeks ago         683.2 MB



% docker run -it -v /Users/downing/cs373/github:/usr/cs373 -w /usr/cs373 gpdowning/python
root@a4fe84a658f0:/usr/cs373# which make
/usr/bin/make



root@a4fe84a658f0:/usr/cs373# make --version
GNU Make 4.0
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2013 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.



root@a4fe84a658f0:/usr/cs373# which git
/usr/bin/git



root@a4fe84a658f0:/usr/cs373# git --version
git version 2.1.4



root@a4fe84a658f0:/usr/cs373# which python3.5
/usr/local/bin/python3.5



root@a4fe84a658f0:/usr/cs373# python3.5 --version
Python 3.5.2



root@a4fe84a658f0:/usr/cs373# which pip3.5
/usr/local/bin/pip3.5



root@a4fe84a658f0:/usr/cs373# pip3.5 --version
pip 8.1.2 from /usr/local/lib/python3.5/site-packages (python 3.5)



root@a4fe84a658f0:/usr/cs373# which pylint
/usr/local/bin/pylint



root@a4fe84a658f0:/usr/cs373# pylint --version
No config file found, using default configuration
pylint 1.6.4,
astroid 1.4.8
Python 3.5.2 (default, Aug  8 2016, 20:46:29)
[GCC 4.9.2]



root@a4fe84a658f0:/usr/cs373# which coverage-3.5
/usr/local/bin/coverage-3.5



root@a4fe84a658f0:/usr/cs373# coverage-3.5 --version
Coverage.py, version 4.2 with C extension
Documentation at https://coverage.readthedocs.io



root@a4fe84a658f0:/usr/cs373# which pydoc3.5
/usr/local/bin/pydoc3.5



root@a4fe84a658f0:/usr/cs373# pydoc3.5 --version
pydoc - the Python documentation tool

pydoc3 <name> ...
    Show text documentation on something.  <name> may be the name of a
    Python keyword, topic, function, module, or package, or a dotted
    reference to a class or function within a module or module in a
    package.  If <name> contains a '/', it is used as the path to a
    Python source file to document. If name is 'keywords', 'topics',
    or 'modules', a listing of these things is displayed.

pydoc3 -k <keyword>
    Search for a keyword in the synopsis lines of all available modules.

pydoc3 -p <port>
    Start an HTTP server on the given port on the local machine.  Port
    number 0 can be used to get an arbitrary unused port.

pydoc3 -b
    Start an HTTP server on an arbitrary unused port and open a Web browser
    to interactively browse documentation.  The -p option can be used with
    the -b option to explicitly specify the server port.

pydoc3 -w <name> ...
    Write out the HTML documentation for a module to a file in the current
    directory.  If <name> contains a '/', it is treated as a filename; if
    it names a directory, documentation is written for all the contents.



root@a4fe84a658f0:/usr/cs373# which autopep8
/usr/local/bin/autopep8



root@a4fe84a658f0:/usr/cs373# autopep8 --version
autopep8 1.2.4



root@a4fe84a658f0:/usr/cs373# pip3.5 list
astroid (1.4.8)
autopep8 (1.2.4)
coverage (4.2)
isort (4.2.5)
lazy-object-proxy (1.2.2)
mccabe (0.5.2)
numpy (1.11.1)
pep8 (1.7.0)
pip (8.1.2)
pylint (1.6.4)
setuptools (20.10.1)
six (1.10.0)
wrapt (1.10.8)



root@a4fe84a658f0:/usr/cs373# cd examples



root@a4fe84a658f0:/usr/cs373/examples# python3.5 Hello.py
Nothing to be done.



root@a4fe84a658f0:/usr/cs373/examples# exit

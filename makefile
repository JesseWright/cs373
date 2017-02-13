.DEFAULT_GOAL := test

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

clean:
	cd examples; make clean
	@echo
	cd exercises; make clean
	@echo
	cd projects/collatz; make clean

config:
	git config -l

docker-build:
	docker build -t gpdowning/python .

docker-pull:
	docker pull gpdowning/python

docker-push:
	docker push gpdowning/python

docker-run:
	docker run -it -v $(PWD):/usr/cs373 -w /usr/cs373 gpdowning/python

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/cs373.git
	git push -u origin master

pull:
	make clean
	@echo
	git pull
	git status

push:
	make clean
	@echo
	git add .gitignore
	git add .travis.yml
	git add Dockerfile
	git add examples
	git add exercises
	git add projects
	git add makefile
	git add notes
	git commit -m "another commit"
	git push
	git status

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

sync:
	@rsync -r -t -u -v --delete              \
    --include "Docker.txt"                   \
    --include "Hello.py"                     \
    --include "Assertions.py"                \
    --include "Exceptions.py"                \
    --include "Types.py"                     \
    --include "Operators.py"                 \
    --include "Variables.py"                 \
    --include "Copy.py"                      \
    --include "Cache.py"                     \
    --exclude "*"                            \
    ../../examples/python/ examples
	@rsync -r -t -u -v --delete              \
    --include "UnitTests1.py"                \
    --include "UnitTests1T.py"               \
    --include "UnitTests2.py"                \
    --include "UnitTests2T.py"               \
    --include "UnitTests3.py"                \
    --include "UnitTests3T.py"               \
    --include "Coverage1.py"                 \
    --include "Coverage1T.py"                \
    --include "Coverage2.py"                 \
    --include "Coverage2T.py"                \
    --include "Coverage3.py"                 \
    --include "Coverage3T.py"                \
    --include "IsPrime1.py"                  \
    --include "IsPrime1T.py"                 \
    --include "IsPrime2.py"                  \
    --include "IsPrime2T.py"                 \
    --include "Factorial.py"                 \
    --include "FactorialT.py"                \
    --include "RMSET.py"                     \
    --include "ReduceT.py"                   \
    --exclude "*"                            \
    ../../exercises/python/ exercises
	@rsync -r -t -u -v --delete              \
    --include "Collatz.py"                   \
    --include "RunCollatz.in"                \
    --include "RunCollatz.py"                \
    --include "RunCollatz.out"               \
    --include "TestCollatz.py"               \
    --include "TestCollatz.out"              \
    --exclude "*"                            \
    ../../projects/python/collatz/ projects/collatz

test:
	make clean
	@echo
	cd examples; make test
	@echo
	cd exercises; make test
	@echo
	cd projects/collatz; make test

versions:
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --version
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	-which $(PYDOC)
	-$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list

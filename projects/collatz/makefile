.PHONY: Collatz.log

.DEFAULT_GOAL := test

FILES :=                              \
    Collatz.html                      \
    Collatz.log                       \
    Collatz.py                        \
    RunCollatz.in                     \
    RunCollatz.out                    \
    RunCollatz.py                     \
    TestCollatz.out                   \
    TestCollatz.py

#    collatz-tests/EID-RunCollatz.in   \
#    collatz-tests/EID-RunCollatz.out  \
#    collatz-tests/EID-TestCollatz.out \
#    collatz-tests/EID-TestCollatz.py  \

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
    PYDOC    := pydoc
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.4
    AUTOPEP8 := autopep8
endif

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

collatz-tests:
	git clone https://github.com/cs373g-fall-2016/collatz-tests.git

Collatz.html: Collatz.py
	pydoc3 -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.tmp: Collatz.py RunCollatz.in RunCollatz.out RunCollatz.py .pylintrc
	-$(PYLINT) Collatz.py
	-$(PYLINT) RunCollatz.py
	$(PYTHON) RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.tmp RunCollatz.out

TestCollatz.tmp: Collatz.py TestCollatz.py .pylintrc
	-$(PYLINT) TestCollatz.py
	$(COVERAGE) run    --branch TestCollatz.py >  TestCollatz.tmp 2>&1
	$(COVERAGE) report -m                      >> TestCollatz.tmp
	cat TestCollatz.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  Collatz.html
	rm -f  Collatz.log
	rm -f  RunCollatz.tmp
	rm -f  TestCollatz.tmp
	rm -rf __pycache__

config:
	git config -l

format:
	$(AUTOPEP8) -i Collatz.py
	$(AUTOPEP8) -i RunCollatz.py
	$(AUTOPEP8) -i TestCollatz.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: Collatz.html Collatz.log RunCollatz.tmp TestCollatz.tmp collatz-tests check

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
	which $(PYDOC)
	$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list

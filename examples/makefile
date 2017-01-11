.DEFAULT_GOAL := test

FILES :=              \
    Hello

#    Exceptions        \
#    Variables         \
#    Copy              \
#    Types             \
#    Operators         \
#    Cache             \
#    Iteration         \
#    Comprehensions    \
#    Yield             \
#    Iterables         \
#    Itertools         \
#    FunctionKeywords  \
#    FunctionDefaults  \
#    FunctionUnpacking \
#    FunctionTuple     \
#    FunctionDict      \
#    Lambdas           \
#    Functions         \
#    Classes           \
#    Callables

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
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

%.pyx: %.py .pylintrc
	-$(PYLINT) $<
	$(PYTHON) $<

clean:
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -rf __pycache__

test: $(FILES:=.pyx)

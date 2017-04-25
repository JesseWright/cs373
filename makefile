.DEFAULT_GOAL := test

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    MYPY     := mypy
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
	git add patterns
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
    --include "Iteration.py"                 \
    --include "Lambdas.py"                   \
    --include "Comprehensions.py"            \
    --include "Yield.py"                     \
    --include "Iterables.py"                 \
    --include "FunctionKeywords.py"          \
    --include "FunctionDefaults.py"          \
    --include "FunctionUnpacking.py"         \
    --include "FunctionTuple.py"             \
    --include "FunctionDict.py"              \
    --include "Callables.py"                 \
    --include "MyPy.py"                      \
    --include "RegExps.py"                   \
    --include "Reflection.py"                \
    --exclude "*"                            \
    ../../examples/python/ examples
	@rsync -r -t -u -v --delete              \
    --include "Bookstore1.dtd.xml"           \
    --include "Bookstore1.xml"               \
    --include "Bookstore2.dtd.xml"           \
    --include "Bookstore3.xml"               \
    --include "Bookstore3.xsd.xml"           \
    --exclude "*"                            \
    ../../examples/xml/ examples
	@rsync -r -t -u -v --delete              \
    --include "Bookstore.json"               \
    --include "Bookstore.schema.json"        \
    --exclude "*"                            \
    ../../examples/json/ examples
	@rsync -r -t -u -v --delete              \
    --include "ShowDatabases.sql"            \
    --include "ShowEngines.sql"              \
    --include "Create.sql"                   \
    --include "Select.sql"                   \
    --include "Join.sql"                     \
    --include "Joins.sql"                    \
    --include "Subqueries.sql"               \
    --include "Sets.sql"                     \
    --include "Aggregation.sql"              \
    --exclude "*"                            \
    ../../examples/sql/ examples
	@rsync -r -t -u -v --delete              \
    --include "MethodOverriding.java"        \
    --include "DynamicBinding.java"          \
    --include "Reflection.java"              \
    --exclude "*"                            \
    ../../examples/java/ examples
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
    --include "Reduce.py"                    \
    --include "ReduceT.py"                   \
    --include "RMSE.py"                      \
    --include "RMSET.py"                     \
    --include "RangeIterator.py"             \
    --include "RangeIteratorT.py"            \
    --include "Map.py"                       \
    --include "MapT.py"                      \
    --include "Range.py"                     \
    --include "RangeT.py"                    \
    --include "Decorators.py"                \
    --include "DecoratorsT.py"               \
    --include "Decorators2.py"               \
    --include "Decorators2T.py"              \
    --include "Select.py"                    \
    --include "SelectT.py"                   \
    --include "Project.py"                   \
    --include "ProjectT.py"                  \
    --include "CrossJoin.py"                 \
    --include "CrossJoinT.py"                \
    --include "ThetaJoin.py"                 \
    --include "ThetaJoinT.py"                \
    --include "NaturalJoin.py"               \
    --include "NaturalJoinT.py"              \
    --exclude "*"                            \
    ../../exercises/python/ exercises
	@rsync -r -t -u -v --delete              \
    --include "StrategyPattern1.java"        \
    --include "StrategyPattern2.java"        \
    --include "StrategyPattern3.java"        \
    --include "StrategyPattern4.java"        \
    --include "StrategyPattern5.java"        \
    --include "StrategyPattern6.java"        \
    --include "SingletonPattern.java"        \
    --include "SingletonPatternT.java"       \
    --include "StrategyPattern7.java"        \
    --include "StrategyPattern8.java"        \
    --include "StrategyPattern9.java"        \
    --include "CreationalPattern.java"       \
    --include "CreationalPatternT.java"      \
    --include "FactoryMethodPattern.java"    \
    --include "FactoryMethodPatternT.java"   \
    --include "AbstractFactoryPattern.java " \
    --include "AbstractFactoryPatternT.java" \
    --include "AdapterPattern.java"          \
    --include "AdapterPatternT.java"         \
    --exclude "*"                            \
    ../../patterns/java/ patterns
	@rsync -r -t -u -v --delete              \
    --include "StrategyPattern9.py"          \
    --exclude "*"                            \
    ../../patterns/python/ patterns
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
	which $(MYPY)
	$(MYPY) --version
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

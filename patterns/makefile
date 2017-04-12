.DEFAULT_GOAL := test

FILES :=             \
    StrategyPattern1 \
    StrategyPattern2 \
    StrategyPattern3 \
    StrategyPattern4 \
    StrategyPattern5 \
    StrategyPattern6

%.class: %.java
	javac -Xlint $<

%.javax: %.class
	java -ea $(patsubst %.class,%,$<)

clean:
	rm -f *.class

test: $(FILES:=.javax)

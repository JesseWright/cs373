%.class: %.java
	javac -Xlint $<

%.javax: %.class
	java -ea $(patsubst %.class,%,$<) < $(patsubst %.class,%,$<).in

clean:
	rm -f *.class

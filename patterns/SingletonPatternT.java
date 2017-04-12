// ----------------------
// SingletonPatternT.java
// ----------------------

// https://en.wikipedia.org/wiki/Singleton_pattern

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

@SuppressWarnings("auxiliaryclass")
public final class SingletonPatternT extends TestCase {
    public void test_1 () {
    	assertEquals(Eager.only(), Eager.only());}

    public void test_2 () {
    	assertEquals( "Eager.f()", Eager.only().f());}

    public void test_3 () {
    	assertEquals(Lazy.only(), Lazy.only());}

    public void test_4 () {
    	assertEquals("Lazy.f()", Lazy.only().f());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(SingletonPatternT.class));}}

/*
% javac -Xlint SingletonPattern.java SingletonPatternT.java

% java -ea SingletonPatternT
....
Time: 0.001

OK (4 tests)

*/

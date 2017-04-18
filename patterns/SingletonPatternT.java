// ----------------------
// SingletonPatternT.java
// ----------------------

// https://en.wikipedia.org/wiki/Singleton_pattern
// https://en.wikipedia.org/wiki/Initialization-on-demand_holder_idiom

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
    	assertEquals(Lazy1.only(), Lazy1.only());}

    public void test_4 () {
    	assertEquals("Lazy1.f()", Lazy1.only().f());}

    public void test_5 () {
    	assertEquals(Lazy2.only(), Lazy2.only());}

    public void test_6 () {
    	assertEquals("Lazy2.f()", Lazy2.only().f());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(SingletonPatternT.class));}}

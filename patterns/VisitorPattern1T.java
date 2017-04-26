// --------------------
// VisitorPattern1T.java
// --------------------

// https://en.wikipedia.org/wiki/Visitor_pattern

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

@SuppressWarnings("auxiliaryclass")
public final class VisitorPattern1T extends TestCase {
    public void test () {
        List<Integer> x    = new Nil<Integer>();
        List<Integer> x4   = new Cons<Integer>(4, x);
        List<Integer> x34  = new Cons<Integer>(3, x4);
        List<Integer> x234 = new Cons<Integer>(2, x34);

        assertSame(2,   x234.first());
        assertSame(x34, x234.rest());

        assertEquals(1, x234.count(3));
        assertEquals(0, x234.count(5));

        assertEquals(0,    x.length());
        assertEquals(1,   x4.length());
        assertEquals(2,  x34.length());
        assertEquals(3, x234.length());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(VisitorPattern1T.class));}}

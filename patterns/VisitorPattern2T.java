// --------------------
// VisitorPattern2T.java
// --------------------

// https://en.wikipedia.org/wiki/Visitor_pattern

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

@SuppressWarnings("auxiliaryclass")
public final class VisitorPattern2T extends TestCase {
    public void test () {
        List<Integer> x    = new Nil<Integer>();
        List<Integer> x4   = new Cons<Integer>(4, x);
        List<Integer> x34  = new Cons<Integer>(3, x4);
        List<Integer> x234 = new Cons<Integer>(2, x34);

        assertSame(2,   x234.first());
        assertSame(x34, x234.rest());

        assertEquals(1, x234.accept(new CountVisitor<Integer>(3)));
        assertEquals(0, x234.accept(new CountVisitor<Integer>(5)));

        assertEquals(0,    x.accept(new LengthVisitor<Integer>()));
        assertEquals(1,   x4.accept(new LengthVisitor<Integer>()));
        assertEquals(2,  x34.accept(new LengthVisitor<Integer>()));
        assertEquals(3, x234.accept(new LengthVisitor<Integer>()));}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(VisitorPattern2T.class));}}

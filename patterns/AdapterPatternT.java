// -------------------
// AdapterPattern.java
// -------------------

// http://en.wikipedia.org/wiki/Adapter_pattern

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

@SuppressWarnings("auxiliaryclass")
public final class AdapterPatternT extends TestCase {
    public void test () {
        Stack<Integer> s = new Stack<Integer>();
        s.push(2);
        s.push(3);
        s.push(4);
        assertEquals(4, (int) s.top());
        s.pop();
        assertEquals(3, (int) s.top());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(AdapterPatternT.class));}}

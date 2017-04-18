// ---------------------
// SingletonPattern.java
// ---------------------

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

class Eager {
    private static final Eager _only = new Eager();

    private Eager ()
        {}

    public static Eager only () {
        return _only;}

    public String f () {
        return "Eager.f()";}}

class Lazy1 {
    private static Lazy1 _only;

    private Lazy1 ()
        {}

    public static Lazy1 only () {
        if (Lazy1._only == null)
            Lazy1._only = new Lazy1();
        return Lazy1._only;}

    public String f () {
        return "Lazy1.f()";}}

class Lazy2 {
    private Lazy2 ()
        {}

    private static class Holder {
        private static final Lazy2 _only = new Lazy2();}

    public static Lazy2 only () {
        return Holder._only;}

    public String f () {
        return "Lazy2.f()";}}

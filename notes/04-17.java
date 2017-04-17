// -----------
// Mon, 17 Apr
// -----------

// design patterns
// 1. strategy
// 2. singleton

class A { // lazy
    private static A x;
    private A () {}
    public static A get () {
        if (x == null)
            x = new A();
        return x;}}

class A { // eager
    public static final A x = new A();
    private A () {}

class T {
    public static void main (...) {
        A x = new A;   // not ok
        A x = A.get(); // lazy
        A x = A.x;     // eager

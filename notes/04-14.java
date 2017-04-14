// -----------
// Fri, 14 Apr
// -----------

class A {
    public        class IC {}
    public static class CC {}

    public        int iv;
    public static int cv;

    void im () {
        ++iv;
        ++cv;
        A t = this;}

    static void cm () {
        ++iv;       // not ok
        ++cv;
        A t = this; // not ok

class T {
    public static void main (...) {
        s.o.p(A.iv); // not ok
        s.o.p(A.cv);
        A.im();      // not ok
        A.cm();
        A x;
        x = new A();
        s.o.p(x.iv);
        s.o.p(x.cv);
        x.im();
        x.cm();

class A {
    void f (int) {}
    void g (long) {}}

class B extends A {
    void f (int) {}
    @override
    void g (int) {}}

class T {
    public static void main (...) {
        B x = new B();
        x.f(2);        // B.f
        x.g(2);        // B.g
        x.g(2L);       // A.g

        A x = new B();
        x.f(2);        // B.f
        x.g(2);        // A.g

abstract class A {
    abstract void f (long);}

class B extends A {  // not ok
    void f (int) {}}

// consequences of an abstract method
// 1. can't implement
// 2. class must become abstract
// 3. children must implement OR become abstract

class T {
    public static void main (...) {
        A x = new B();
        x.f(2);        // B.f

abstract class A {
             void f (int) {}
    final    void g (int) {}
    abstract void h (int);}

class B extends A {
    ???

// children can optionally implement f
// children can not implement g
// children must implement h OR become abstract

class A {
    void f (int) {}}

class B extends A {
    void f (int) {}}

class T {
    public static void main (...) {
        A x;
        if (...)
            x = new A();
        else
            x = new B();
        x.f(2);

// no dynamic binding
// 1. private method
// 2. static method
// 3. final class
// 4. final method

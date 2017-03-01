# Java

class A {
    public int i;

    public class B {
        public int j;

        public void g () {
            S.O.P(this.j);
            S.O.P(A.this.i);}}

    public static class C {}}

class T {
    public static void main (...) {
        A x = new A();
        S.O.P(x.i);

        A.B y = x.new B();
        y.g();
        A.B t = x.new B();
        t.g();

        A.C z = new A.C();

class LinkedList {
    private static class Node {...}
    private        class Iter implements Iterator {...}

    public Iterator iterator () {
        return new Iter();}}

class T {
    public static void main (...) {
        LL x = new LL(...)
        Iterator p = x.iterator();
        while (p.hasNext()) {
            ...p.next()...}}}

// ---------------------
// MethodOverriding.java
// ---------------------

class A {
    public String f (int i) {
        return "A.f";}

    public String g (int l) {
        return "A.g";}}

class B extends A {
    public String f (int i) {
        return "B.f";}

    public String g (long i) {
        return "B.g";}}

final class MethodOverriding {
    public static void main (String[] args) {
        System.out.println("MethodOverriding.java");

        B x = new B();

        assert x.f(2)  == "B.f";
        assert x.g(2)  == "A.g";
        assert x.g(2L) == "B.g";

        A y = new B();

        assert y.f(2)  == "B.f";
        assert y.g(2)  == "A.g";
//      assert y.g(2L) == "A.g"; // error: incompatible types: possible lossy conversion from long to int

        System.out.println("Done.");}}

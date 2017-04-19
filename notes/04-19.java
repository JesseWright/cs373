// -----------
// Mon, 17 Apr
// -----------

// in Python
// print(type(2))    # int
// print(type(int))  # type
// print(type(type)) # type

// class A :
//     ...
// t = type(A)
// x = A()
// y = t()

class A {
    ...}

class T {
    public static void main () {
        Class  c = A.class;
        A      x = new A();
        Class  c = x.getClass();
        Class  c = Class.forName("A"); // not name of class?
        Object y = c.newInstance();    // private constr?
                                       // abstract class?
                                       // interface?
        A      z = (A) y;              // cast?














// -----------
// Wed, 19 Apr
// -----------

/*
Python

print(type(2))    # int
print(type(int))  # type
print(type(type)) # type

class A :
    ...

x = A()
t = type(A)
y = t()
*/

class A
    A (...) {...}}

class T {
    public static void main (...) {
        A      x = new A();
        Class  c = A.class;            // Class is a type
                                       // class is a static data member of Object
        Class  d = x.getClass();
        Class  e = Class.forName("A"); // forName is a static method
                                       // A might not exist?
        Object y = e.newInstance();    // no default constr?
                                       // A is an abstract class?
                                       // A is an interface?
                                       // private constr?
        A      z = (A)y;               // cast?

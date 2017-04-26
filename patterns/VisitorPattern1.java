// --------------------
// VisitorPattern1.java
// --------------------

interface List<T> {
    int     count  (T v);
    T       first  ();
    int     length ();
    List<T> rest   ();}

class Cons<T> implements List<T> {
    private T       _first;
    private List<T> _rest;

    public Cons (T first, List<T> rest) {
        _first = first;
        _rest  = rest;}

    public int count (T v) {
        if (_first == v)
            return 1 + _rest.count(v);
        return _rest.count(v);}

    public T first () {
        return _first;}

    public int length () {
        return 1 + _rest.length();}

    public List<T> rest () {
        return _rest;}}

class Nil<T> implements List<T> {
    public int count (T v) {
        return 0;}

    public T first () {
        throw new RuntimeException();}

    public int length () {
        return 0;}

    public List<T> rest () {
        return this;}}

// --------------------
// VisitorPattern1.java
// --------------------

interface List<T> {
    int     accept (Visitor<T> v);
    T       first  ();
    List<T> rest   ();}

class Cons<T> implements List<T> {
    private T       _first;
    private List<T> _rest;

    public Cons (T first, List<T> rest) {
        _first = first;
        _rest  = rest;}

    public int accept (Visitor<T> v) {
        return v.visit(this);}

    public T first () {
        return _first;}

    public List<T> rest () {
        return _rest;}}

class Nil<T> implements List<T> {
    public int accept (Visitor<T> v) {
        return v.visit(this);}

    public T first () {
        throw new RuntimeException();}

    public List<T> rest () {
        return this;}}

interface Visitor<T> {
    int visit (Cons<T> c);
    int visit (Nil<T>  n);}

class CountVisitor<T> implements Visitor<T> {
    private T _v;

    public CountVisitor (T v) {
        _v = v;}

    public int visit (Cons<T> c) {
        if (c.first() == _v)
            return 1 + c.rest().accept(this);
        return c.rest().accept(this);}

    public int visit (Nil<T> n) {
        return 0;}}

class LengthVisitor<T> implements Visitor<T> {
    public int visit (Cons<T> c) {
        return 1 + c.rest().accept(this);}

    public int visit (Nil<T> n) {
        return 0;}}

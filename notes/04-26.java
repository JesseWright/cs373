// -----------
// Wed, 26 Apr
// -----------

interface List<T> {
    T       first  ();
    List<T> rest   ();
    int     length ();
    int     count  (T v);}

class Nil<T> implements List<T> {
    T       first ()    {throw ...;}
    List<T> rest ()     {return this;}
    int     length ()   {return 0;}
    int     count (T v) {return 0;}}

class Cons<T> implements List<T> {
    T       _f;
    List<T> _r;

    Cons (T f, List<T> r) {
        _f = f;
        _r = r;}

    T first () {
        return _f;}

    List<T> rest () {
        return _r;}

    int length () {
        return 1 + _r.length();}

    int count (T v) {
        if (Objects.equals(_f, v))
            return 1 + _r.count(v);
        return _r.count();}

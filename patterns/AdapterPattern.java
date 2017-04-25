// -------------------
// AdapterPattern.java
// -------------------

import java.util.ArrayList;
import java.util.List;

class Stack<T> {
    private List<T> _a;

    public Stack () {
        _a = new ArrayList<T>();}

    public Boolean empty () {
        return _a.isEmpty();}

    public void pop () {
        _a.remove(_a.size() - 1);}

    public void push (T v) {
        _a.add(v);}

    public T top () {
        return _a.get(_a.size() - 1);}}

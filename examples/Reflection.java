// ---------------
// Reflection.java
// ---------------

interface I
    {}

interface J extends I
    {}

abstract class A implements I
    {}

class B
    {}

class C implements I {
    public C (int i)
        {}}

class D implements I {
    private D ()
        {}}

class E implements I
    {}

final class Reflection {
    public static void main (String[] args) {
        System.out.println("Reflection.java");

        try {
            I x = (I) Class.forName("J").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException: J");}

        try {
            I x = (I) Class.forName("A").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException");}

        try {
            I x = (I) Class.forName("B").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert e.toString().equals("java.lang.ClassCastException: B cannot be cast to I");}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}

        try {
            I x = (I) Class.forName("C").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert e.toString().equals("java.lang.InstantiationException: C");}

       try {
            I x = (I) Class.forName("D").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert e.toString().equals("java.lang.IllegalAccessException: Class Reflection can not access a member of class D with modifiers \"private\"");}
        catch (InstantiationException e) {
            assert false;}

        try {
            I x = (I) Class.forName("E").newInstance();
            assert x.getClass() == E.class;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert false;}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}

        try {
            Object x = Class.forName("F").newInstance();
            assert false;}
        catch (ClassCastException e) {
            assert false;}
        catch (ClassNotFoundException e) {
            assert e.toString().equals("java.lang.ClassNotFoundException: F");}
        catch (IllegalAccessException e) {
            assert false;}
        catch (InstantiationException e) {
            assert false;}

        System.out.println("Done.");}}

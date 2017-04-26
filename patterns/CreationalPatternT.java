// -----------------------
// CreationalPatternT.java
// -----------------------

// https://en.wikipedia.org/wiki/Creational_pattern

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

@SuppressWarnings("auxiliaryclass")
public final class CreationalPatternT extends TestCase {
    public void test_1 () {
        Maze m = Game.createMaze();
        assertEquals(Maze.class,         m.getClass());
        assertEquals(Room.class, m.room(0).getClass());
        assertEquals(Door.class, m.door(0).getClass());}

    public void test_2 () {
        Maze m = Game.createEnchantedMaze();
        assertEquals(Maze.class,                  m.getClass());
        assertEquals(EnchantedRoom.class, m.room(0).getClass());
        assertEquals(EnchantedDoor.class, m.door(0).getClass());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(CreationalPatternT.class));}}

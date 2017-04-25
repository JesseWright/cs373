// --------------------------
// FactoryMethodPatternT.java
// --------------------------

// http://en.wikipedia.org/wiki/Factory_method_pattern

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

@SuppressWarnings("auxiliaryclass")
public final class FactoryMethodPatternT extends TestCase {
    public void test_1 () {
        Game g = new Game();
        Maze m = g.createMaze();
        assertEquals(Game.class,         g.getClass());
        assertEquals(Maze.class,         m.getClass());
        assertEquals(Room.class, m.room(0).getClass());
        assertEquals(Door.class, m.door(0).getClass());}

    public void test_2 () {
        Game g = new EnchantedGame();
        Maze m = g.createMaze();
        assertEquals(EnchantedGame.class, g.getClass());
        assertEquals(Maze.class,          m.getClass());
        assertEquals(EnchantedRoom.class, m.room(0).getClass());
        assertEquals(EnchantedDoor.class, m.door(0).getClass());}

    public static void main (String[] args) {
        TestRunner.run(new TestSuite(FactoryMethodPatternT.class));}}

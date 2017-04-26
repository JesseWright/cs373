// ----------------------------
// AbstractFactoryPatternT.java
// ----------------------------

// https://en.wikipedia.org/wiki/Abstract_factory_pattern

@SuppressWarnings("auxiliaryclass")
final class AbstractFactoryPatternT {
    public static void main (String[] args) {
        System.out.println("AbstractFactoryPatternT.java");

        {
        MazeFactory mf = new MazeFactory();
        Maze        m  = Game.createMaze(mf);
        assert mf.getClass()        == MazeFactory.class;
        assert m.getClass()         == Maze.class;
        assert m.room(0).getClass() == Room.class;
        assert m.door(0).getClass() == Door.class;
        }

        {
        MazeFactory mf = new EnchantedMazeFactory();
        Maze        m  = Game.createMaze(mf);
        assert mf.getClass()        == EnchantedMazeFactory.class;
        assert m.getClass()         == Maze.class;
        assert m.room(0).getClass() == EnchantedRoom.class;
        assert m.door(0).getClass() == EnchantedDoor.class;
        }

        System.out.println("Done.");}}

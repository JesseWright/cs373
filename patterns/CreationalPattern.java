// ----------------------
// CreationalPattern.java
// ----------------------

import java.util.ArrayList;
import java.util.List;

class Room {}
class EnchantedRoom extends Room {}

class Door {
    private Room _r;
    private Room _s;

    public Door (Room r, Room s) {
        _r = r;
        _s = s;}}

class EnchantedDoor extends Door {
    public EnchantedDoor (Room r, Room s) {
        super(r, s);}}

final class Maze {
    private List<Room> _rooms = new ArrayList<Room>();
    private List<Door> _doors = new ArrayList<Door>();

    public void addRoom (Room r) {
        _rooms.add(r);}

    public void addDoor (Door d) {
        _doors.add(d);}

    public Room room (int i) {
        return _rooms.get(i);}

    public Door door (int i) {
        return _doors.get(i);}}

abstract class Game {
    public static Maze createMaze () {
        Maze m = new Maze();
        m.addRoom(new Room());
        m.addRoom(new Room());
        m.addRoom(new Room());
        m.addDoor(new Door(m.room(0), m.room(1)));
        m.addDoor(new Door(m.room(1), m.room(2)));
        return m;}

    public static Maze createEnchantedMaze () {
        Maze m = new Maze();
        m.addRoom(new EnchantedRoom());
        m.addRoom(new EnchantedRoom());
        m.addRoom(new EnchantedRoom());
        m.addDoor(new EnchantedDoor(m.room(0), m.room(1)));
        m.addDoor(new EnchantedDoor(m.room(1), m.room(2)));
        return m;}}

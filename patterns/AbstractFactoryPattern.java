// ---------------------------
// AbstractFactoryPattern.java
// ---------------------------

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

class MazeFactory {
    public Room makeRoom () {
        return new Room();}

    public Door makeDoor (Room r, Room s) {
        return new Door(r, s);}}

class EnchantedMazeFactory extends MazeFactory {
    public EnchantedRoom makeRoom () {
        return new EnchantedRoom();}

    public EnchantedDoor makeDoor (Room r, Room s) {
        return new EnchantedDoor(r, s);}}

abstract class Game {
    public static Maze createMaze (MazeFactory mf) {
        Maze m = new Maze();
        m.addRoom(mf.makeRoom());
        m.addRoom(mf.makeRoom());
        m.addRoom(mf.makeRoom());
        m.addDoor(mf.makeDoor(m.room(0), m.room(1)));
        m.addDoor(mf.makeDoor(m.room(1), m.room(2)));
        return m;}}

// -----------
// Mon, 24 Apr
// -----------

abstract class Game {
    static Maze createMaze (MazeFactory mf) {
        ...mf.getRoom()...
        ...mf.getDoor()...

class MazeFactory {
    Room getRoom () {
        return new Room();}
    ...}

class EnchantedMazeFactory exteds MazeFactory {
    EnchantedRoom getRoom () {
        return new EnchantedRoom();}
    ...}

class Stack<T> {
    private List<T> x;
    public Stack () {
        x = new ArrayList<T>();}
    public void pop (T v) {
        // remove from the back of the ArrayList: O(1)
    public void push (T v) {
        // add    to   the back of the ArrayList: amortized O(1)

class Queue<T> {
    private List<T> x;
    public Stack () {
        x = new LinkedList<T>();}
    public void pop (T v) {
        // remove from the front of the LinkedList: O(1)
    public void push (T v) {
        // add    to   the back  of the LinkedList: O(1)

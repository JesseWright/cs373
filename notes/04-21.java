// -----------
// Fri, 21 Apr
// -----------

// return types are covariant

class Game {
    Maze createMaze () {
        ...getRoom()...

    Room getRoom () {
        return new Room();}}

class EnchantedGame extends Game {
    EnchantedRoom getRoom () {
        return new EnchantedRoom();}}

class T {
    public static void main (...) {
        EnchantedGame x = new EnchantedGame();
        EnchantedRoom y = x.getRoom();

// -----------
// Wed, 12 Apr
// -----------

class Movie {
    public Movie (String title, int priceCode) {
        ...}}

class RegulareMovie extends Movie {
    public RegulareMovie (String title) {
        super(title, Movie.Regular)}

    public int getCharge () {
        ...}}

abstract class Price {
    abstract int getCharge ();}

class RegularePrice extends Price {
    public int getCharge () {
        ...}}

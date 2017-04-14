// -----------
// Wed, 12 Apr
// -----------

class Movie {
    public Movie (String title, int priceCode) {
        ...}}

class RegularMovie extends Movie {
    public RegularMovie (String title) {
        super(title, Movie.Regular)}

    public int getCharge () {
        ...}}

x.addRental(new Rental(new Movie("Shane", Movie.REGULAR), 2));

// would become

x.addRental(new Rental(new RegularMovie("Shane")));

abstract class Price {
    abstract int getCharge ();}

class RegularPrice extends Price {
    public int getCharge () {
        ...}}

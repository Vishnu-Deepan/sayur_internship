public class Restaurant {
    private String name;
    private String cuisineType;
    private double rating;
    private List<String> menu;
    private List<String> customers;

    public Restaurant(String name, String cuisineType, double rating) {
        this.name = name;
        this.cuisineType = cuisineType;
        this.rating = rating;
        this.menu = new ArrayList<>();
        this.customers = new ArrayList<>();
    }

    public void setRating(double newRating) {
        this.rating = newRating;
    }

    public double getRating() {
        return this.rating;
    }

    public void addToMenu(String item) {
        this.menu.add(item);
    }

    public List<String> getMenu() {
        return this.menu;
    }

    public void welcomeCustomer(String customerName) {
        this.customers.add(customerName);
    }

    public List<String> listCustomers() {
        return this.customers;
    }

    public String orderDish(String dishName) {
        String message = prepareDish(dishName);
        return "Order placed: " + message;
    }

    private String prepareDish(String dishName) {
        return "Preparing " + dishName + "...";
    }
}

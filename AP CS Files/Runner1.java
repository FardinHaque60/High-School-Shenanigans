public class Runner1 {
    public static void main(String[] args) {
        Warrior bob = new Warrior("bob", 5, 3);
        bob.printInfo();
        if (bob.fight(30, 60))
            System.out.print("Bob won the fight");
        else 
            System.out.println("Bob lost the fight");
    }
}
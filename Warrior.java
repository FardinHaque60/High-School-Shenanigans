public class Warrior {
    private String name;
    private int power;
    private int lives;

    public Warrior(String n, int p, int l) {
        name = n;
        power = p;
        lives = l;
    }

    public boolean fight(double attack, double attack2) {
        if (attack > attack2)
            return true;
        else
            return false;
    }

    public void hearts(double attack, double attack2) {
        if (fight(attack, attack2)) {
            power += 5;
            System.out.println("Lives: " + lives);
        }
        else {
            lives--;
            System.out.println("Lives " + lives);
        }
    }

    public void printInfo() {
        System.out.println("Name: " + name);
        System.out.println("Power: " + power);
        System.out.println("Lives: " + lives);
    }
}
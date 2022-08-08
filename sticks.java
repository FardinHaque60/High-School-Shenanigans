import java.util.Scanner; 

public class sticks 
{
    public static void main(String[] args) {

        Scanner reader = new Scanner(System.in);
        int sticks = (int)(Math.random()*10)+21;
        System.out.println("There are " + sticks + " sticks. ");
        System.out.println("Select 1 to go first, select 2 to go second.");
        boolean turn; //true means player turn, false means computer
        if(reader.nextInt() == 1) 
            turn = true;
        else 
            turn = false;
        
           
        //game stops when we get to 0 sticks 
        //so the game must continue to run as long as the number of sticks > 0 
        while(sticks > 0){
            if(turn)
                sticks = playerMove(sticks, reader);
            else
                sticks = computerMove(sticks);
            System.out.println("There are " + sticks + " sticks left.");
              if(sticks == 0 && turn) //&& means "AND"
                    System.out.println("Player wins!"); 
              if(sticks == 0 && !turn) //! means "NOT"
                    System.out.println("Computer wins."); 
              turn = !turn; 
        }
    }

    public static int playerMove(int sticks, Scanner reader) {
        System.out.println("Select  how many sticks to take."); 
        int take = reader.nextInt();
        if(take < 1)
            take = 1; 
        if(take > 3)
            take = 3; 
        if(take > sticks)
            take = sticks;
        System.out.println("You took " + take + " sticks."); 
        return sticks - take; //this is the int that is being returned 
    }

    public static int computerMove(int sticks){
        int take; 
        if(sticks % 4 != 0)   //if number of sticks is not a multiple of 4
            take = sticks % 4; 
        else    //number of sticks is a multiple of 4
            take = (int)(Math.random()*3) + 1; 
        System.out.println("The computer took " + take + " sticks."); 
        return sticks - take; 
    }
    /*
    public static void main(String[] args) {

        for(int i = 0; i < 15; i++)
        System.out.println((int)(Math.random()*10));

    }
    */
} 
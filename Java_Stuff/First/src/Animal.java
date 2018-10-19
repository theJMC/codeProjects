//Single Line Comment 

import java.util.Scanner;

public class Animal {

	public static final double FAVNUMEBER = 3.141692;
	
	private String name;
	private int weight;
	private boolean hasOwner = false ;
	private byte age;
	private long uniqueID;
	private char favChar;
	private double speed;
	private float height;
	
	protected static int numberOfAnimals = 0;
	
	static Scanner userinput = new Scanner(System.in);

	public Animal() {
		numberOfAnimals++;
		
		int sumOfNumbers = 5+1;
		System.out.println("5+1=" + sumOfNumbers);
		
		System.out.print("Enter a name: ");
		
		if (userinput.hasNextLine()) {
			
		 
			
		}
	}
			
	public static void main(String[] args) {
		
		Animal theAnimal = new Animal();
		
	}
}

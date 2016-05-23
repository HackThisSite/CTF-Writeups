package exploit;

import java.util.Scanner;

public class KeithLikesToTroll {
	public static void main(String[] args){
		int key;

		Scanner scn = new Scanner(System.in);
		System.out.print("Enter key: ");
		key = scn.nextInt();
		scn.close();

		if(1338557220 / key * key != 1338557220 && key > 0){
			System.out.println("Login succesful. The flag is the smallest key which will let you log in.");
		}else{
			System.out.println("Login rejected.");
		}
	}
}

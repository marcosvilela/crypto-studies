import java.util.Scanner;

public class Cifra {

	public static void cifrar(String m){
		char[] palavra = new char[m.length()];  //cria um armazenamento para a palavra
		for(int i = 0; i<palavra.length; i++){
			palavra = m.toCharArray();
			int c = palavra[i];
			if(c != 32){ //impede de trocar os espaços para #
			c+=3;
			}
			System.out.print((char)c);
		}
	}
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite a mensagem a ser cifrada:");
		Cifra.cifrar(sc.nextLine());
		sc.close();
	}
}

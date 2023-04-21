import javax.swing.JOptionPane;

public class Q01
{
	public static void main(String[] args)
	{
		String nome = JOptionPane.showInputDialog(null, "Informe seu nome: ");
		String idadeAnos = JOptionPane.showInputDialog(null, "Informe sua idade em anos: ");
		   		
		double n1 = Double.valueOf(idadeAnos).doubleValue();
		
		double soma = n1*365;
		String s = String.valueOf(soma);
		    		
		JOptionPane.showMessageDialog(null, "A idade em dias de " + nome + " é "+ s+ " (dias)");
	}
}
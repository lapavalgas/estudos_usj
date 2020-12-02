import javax.swing.JOptionPane;

public class Main {

	public static void main(String[] args) {
		PessoaIMC[] lstPessoa;
		int tamanhoVetor = Integer.parseInt(JOptionPane.showInputDialog("Quantas pessoas serão cadastradas?"));
		lstPessoa = new PessoaIMC[tamanhoVetor];
		for (int i = 0; i < tamanhoVetor; i++) {
			int tipoObjeto = Integer.parseInt(JOptionPane.showInputDialog(
					"Digite 0 para cadastrar pessoas do sexo masculino e 1 para cadastrar pessoas do sexo feminino."));
			while (tipoObjeto <= -1 && tipoObjeto >= 2) {
				tipoObjeto = Integer.parseInt(JOptionPane.showInputDialog(
						"Digite 0 para cadastrar pessoas do sexo masculino e 1 para cadastrar pessoas do sexo feminino."));
			}
			if (tipoObjeto == 0) {
				String nome = JOptionPane.showInputDialog("Digite o nome desse cara...");
				String data = JOptionPane.showInputDialog("Digite a data de nascimento de " + nome);
				double peso = Double.parseDouble(JOptionPane.showInputDialog("Digite o peso do " + nome));
				double altura = Double.parseDouble(JOptionPane.showInputDialog("Digite a altura do " + nome));
				Homem obj = new Homem(nome, data, peso, altura);
				lstPessoa[i] = obj;
			} else if (tipoObjeto == 1) {
				String nome = JOptionPane.showInputDialog("Digite o nome dessa guria...");
				String data = JOptionPane.showInputDialog("Digite a data de nascimento da " + nome);
				double peso = Double.parseDouble(JOptionPane.showInputDialog("Digite o peso da " + nome));
				double altura = Double.parseDouble(JOptionPane.showInputDialog("Digite a altura da " + nome));
				Mulher obj = new Mulher(nome, data, peso, altura);
				lstPessoa[i] = obj;
			}
		}
		for (int i = 0; i < tamanhoVetor; i++) {
			System.out.println("posição: " + i + "\n" + lstPessoa[i].toString() + "\n" + lstPessoa[i].resultIMC());
			System.out.println("--=--=--=--=--=--=--=--=--=--=--=--=--=--");
		}
	}
}

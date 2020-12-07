public class Pessoa {
	private String nome;
	private String dataNasc;

	public Pessoa(String nome, String dataNascimento) {
		this.nome = nome;
		this.dataNasc = dataNascimento;
	}

	public String getNome() {
		return nome;
	}

	public String getDataNascimento() {
		return dataNasc;
	}

	@Override
	public String toString() {
		return "Nome: " + nome + "\nDataNascimento: " + dataNasc;
	}
}

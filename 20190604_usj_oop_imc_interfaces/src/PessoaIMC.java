public abstract class PessoaIMC extends Pessoa {
	private double peso;
	private double altura;

	public PessoaIMC(String nome, String dataNasc, double peso, double altura) {
		super(nome, dataNasc);
		this.peso = peso;
		this.altura = altura;
	}

	public double getPeso() {
		return peso;
	}

	public double getAltura() {
		return altura;
	}

	public double calculaIMC(double peso, double altura) {
		return (peso / (altura * altura));
	}

	public abstract String resultIMC();

	@Override
	public String toString() {
		return "Nome: " + this.getNome() + "\nDataNascimento: " + this.getDataNascimento() + "\npeso: " + peso
				+ "\naltura: " + altura;
	}
}

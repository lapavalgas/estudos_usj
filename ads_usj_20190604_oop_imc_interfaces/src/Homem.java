public class Homem extends PessoaIMC {

	public Homem(String nome, String dataNasc, double peso, double altura) {
		super(nome, dataNasc, peso, altura);
	}

	public String resultIMC() {
		double imc = calculaIMC(this.getPeso(), this.getAltura());
		String resultadoIMC = "algum problema nos dados fornecidos";
		if (imc < 20.7) {
			resultadoIMC = "IMC: " + imc + " : Abaixo do peso ideal.";
		} else if (imc > 20.7 && imc < 26.4) {
			resultadoIMC = "IMC: " + imc + " : Peso ideal.";
		} else if (imc > 26.4) {
			resultadoIMC = "IMC: " + imc + " : Acima do peso ideal.";
		}
		return resultadoIMC;
	}
}

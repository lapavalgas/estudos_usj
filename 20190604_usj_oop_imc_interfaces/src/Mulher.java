public class Mulher extends PessoaIMC {

	public Mulher(String nome, String dataNasc, double peso, double altura) {
		super(nome, dataNasc, peso, altura);
	}

	public String resultIMC() {
		double imc = calculaIMC(this.getPeso(), this.getAltura());
		System.out.println(imc);
		String resultadoIMC = "algum problema nos dados fornecidos";
		if (imc < 19) {
			resultadoIMC = "IMC: " + imc + " : Abaixo do peso ideal.";
		} else if (imc > 19 && imc < 25.8) {
			resultadoIMC = "IMC: " + imc + " : Peso ideal.";
		} else if (imc > 25.8) {
			resultadoIMC = "IMC: " + imc + " : Acima do peso ideal.";
		}
		return resultadoIMC;
	}
}

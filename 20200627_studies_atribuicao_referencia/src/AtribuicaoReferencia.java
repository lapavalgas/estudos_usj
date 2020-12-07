public class AtribuicaoReferencia {
    public static void main(String[] args) throws Exception {
        // tipos primitivos -> atribuição por valor (por cópia!)
        // byte, short, int, long
        // float e double
        // boolean
        // char
        int a = 1;
        int b = a;
        System.out.println(a +" "+ b);
        a++;
        b--;
        System.out.println(a +" "+ b);
        
        // tipos compostos -> atribuição por referencia
        Produto p1 = new Produto("Banana");
        Produto p2 = p1;
        System.out.println(p1.nome +" "+ p2.nome);
        p1.nome = "Maça";
        System.out.println(p1.nome +" "+ p2.nome);

    }
}

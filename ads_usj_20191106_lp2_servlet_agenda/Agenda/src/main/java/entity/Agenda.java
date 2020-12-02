package entity;

import java.util.ArrayList;
import java.util.List;

public class Agenda {

    List<Contato> contatos;

    public Agenda() {
        this.contatos = new ArrayList<>();
    }

    public void toAgenda(String nome, String telefone) {
        this.contatos.add(new Contato(nome, telefone));
    }
    public void toAgenda(Contato contato) {
        this.contatos.add(contato);
    }

    public List<Contato> getContatos() {
        return this.contatos;
    }   
    

}
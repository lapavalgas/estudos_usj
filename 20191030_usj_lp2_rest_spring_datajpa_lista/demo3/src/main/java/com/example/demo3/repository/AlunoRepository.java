package com.example.demo3.repository;

import com.example.demo3.model.Aluno;

import org.springframework.data.repository.CrudRepository;

// This will be AUTO IMPLEMENTED by Spring into a Bean called AlunoRepository
// CRUD refers Create, Read, Update, Delete

public interface AlunoRepository extends CrudRepository<Aluno, Integer> {

    Aluno findByLastName(String lastName);

    Aluno findById(long id);

}   

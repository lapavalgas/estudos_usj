package com.disciplina.atividade01;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputDigito;
    private Button btnVerificar;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
          inputDigito = findViewById(R.id.inputDigito);
          btnVerificar = findViewById(R.id.btnVerificar);
          TextView textResult = findViewById(R.id.textViewResult);


        btnVerificar.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Integer valorAnterior = Integer.parseInt(inputDigito.getText().toString());
                valorAnterior = valorAnterior - 1;
                textResult.setText(valorAnterior.toString());
            }
        });
    }
}
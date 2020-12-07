package com.disciplina.atividade08;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputSalarioFixo;
    private EditText inputValorTotalVendas;
    private Button btnCalcular;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputSalarioFixo = findViewById(R.id.inputSalarioFixo);
        inputValorTotalVendas = findViewById(R.id.inputValorTotalVendas);
        btnCalcular = findViewById(R.id.btnCalcular);
        textResult = findViewById(R.id.textResult);

        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Double salarioFixo = Double.parseDouble(inputSalarioFixo.getText().toString());
                Double valorTotalDeVendas = Double.parseDouble(inputValorTotalVendas.getText().toString());
                Double salarioTotal = 0.0;
                if (valorTotalDeVendas > 1500.0) {
                    salarioTotal = salarioFixo + ((salarioFixo*5)/100);
                } else {
                    salarioTotal = salarioFixo + ((salarioFixo *3)/100);
                }
                textResult.setText(salarioTotal.toString());
            }
        });
    }
}
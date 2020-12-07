package com.disciplina.atividade05;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputPrecoFabrica;
    private Button btnCalcularPrecoFinal;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputPrecoFabrica = findViewById(R.id.inputPrecoFabrica);
        btnCalcularPrecoFinal = findViewById(R.id.btnCalcularPrecoFinal);
        textResult = findViewById(R.id.textResult);

        btnCalcularPrecoFinal.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Double precoFabrica = Double.parseDouble(inputPrecoFabrica.getText().toString());
                Double percentualDistribuidor = precoFabrica * 0.28;
                Double percentualImposto = precoFabrica * 0.45;
                Double valorFinal = precoFabrica + percentualDistribuidor + percentualImposto;
                textResult.setText(valorFinal.toString());
            }
        });
    }
}
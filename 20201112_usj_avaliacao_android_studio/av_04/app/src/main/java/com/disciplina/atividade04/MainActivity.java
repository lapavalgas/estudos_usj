package com.disciplina.atividade04;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputSalarioMensal;
    private EditText inputAjustes;
    private Button btnCalcular;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputSalarioMensal = findViewById(R.id.inputSalarioMensal);
        inputAjustes = findViewById(R.id.inputAjuste);
        btnCalcular = findViewById(R.id.btnCalcular);
        textResult = findViewById(R.id.textResult);

        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Double salarioMensal = Double.parseDouble(inputSalarioMensal.getText().toString());
                Double valorReajuste = (salarioMensal* Double.parseDouble(inputAjustes.getText().toString())) /100;
                Double novoSalario = salarioMensal + valorReajuste;
                textResult.setText(novoSalario.toString());
            }
        });
    }
}
package com.disciplina.atividade07;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputNumeroHoraTrabalhadas;
    private EditText inputSalarioPorHora;
    private Button btnCalcular;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputNumeroHoraTrabalhadas = findViewById(R.id.inputNumeroHoraTrabalhadas);
        inputSalarioPorHora = findViewById(R.id.inputSalarioPorHora);
        btnCalcular = findViewById(R.id.btnCalcular);
        textResult = findViewById(R.id.textResult);

        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Double totalHorasTrabalhadas = Double.parseDouble(inputNumeroHoraTrabalhadas.getText().toString());
                Double salarioPorHora = Double.parseDouble(inputSalarioPorHora.getText().toString());
                Double quarentaHoras = 0.0;
                Double valorSalariBase = 0.0;
                Double qntdHoraExtra = 0.0;
                Double valorHoraExtra = 0.0;
                Double salarioBrutoTotal = 0.0;

                if (totalHorasTrabalhadas > 40) {
                    quarentaHoras = 40.0;
                    qntdHoraExtra = totalHorasTrabalhadas - quarentaHoras;
                    valorSalariBase = quarentaHoras * salarioPorHora;
                    valorHoraExtra =  (qntdHoraExtra * salarioPorHora) + (((qntdHoraExtra * salarioPorHora)*50)/100);
                } else {
                    quarentaHoras = totalHorasTrabalhadas;
                    valorSalariBase = quarentaHoras * salarioPorHora;
                }
                salarioBrutoTotal = valorSalariBase + valorHoraExtra;

                textResult.setText(salarioBrutoTotal.toString());



            }
        });





    }
}
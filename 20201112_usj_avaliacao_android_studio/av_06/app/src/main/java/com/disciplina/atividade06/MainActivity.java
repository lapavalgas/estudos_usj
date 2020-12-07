package com.disciplina.atividade06;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputTotalCarrosVendidos;
    private EditText inputValorTotalVendas;
    private EditText inputSalarioFixo;
    private EditText inputValorComissao;
    private Button btnCalcular;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputTotalCarrosVendidos = findViewById(R.id.inputTotalCarrosVendidos);
        inputValorTotalVendas = findViewById(R.id.inputValorTotalVendas);
        inputSalarioFixo = findViewById(R.id.inputSalarioFixo);
        inputValorComissao = findViewById(R.id.inputPercentualPorVenda);
        btnCalcular = findViewById(R.id.btnCalcular);
        textResult = findViewById(R.id.textResult);

         btnCalcular.setOnClickListener(new View.OnClickListener() {
             @Override
             public void onClick(View v) {
                 Double totalCarrosVendidos = Double.parseDouble(inputTotalCarrosVendidos.getText().toString());
                 Double totalVendas = Double.parseDouble(inputValorTotalVendas.getText().toString());
                 Double salarioFixo = Double.parseDouble(inputSalarioFixo.getText().toString());
                 Double percentualPorCarro = Double.parseDouble(inputValorComissao.getText().toString());
                 Double PERCENTUAL_FIXO = 5.0;

                 Double valorExtraPorCarroVendido = 0.0;
                 for (int i=0; i < totalCarrosVendidos; i++) {
                     valorExtraPorCarroVendido += (totalVendas*(5+percentualPorCarro))/100;
                 }
                 Double salarioTotal = salarioFixo + valorExtraPorCarroVendido;
                textResult.setText(salarioTotal.toString());
             }
         });
    }
}
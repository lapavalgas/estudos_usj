package com.disciplina.avaliao09;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputNumeroConta;
    private EditText inputSaldo;
    private EditText inputDebito;
    private EditText inputCredito;
    private Button btnCalcular;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputNumeroConta = findViewById(R.id.inputNumeroConta);
        inputSaldo = findViewById(R.id.inputSaldo);
        inputDebito = findViewById(R.id.inputDebito);
        inputCredito = findViewById(R.id.inputCredito);
        btnCalcular = findViewById(R.id.btnCalcular);
        textResult = findViewById(R.id.textResult);


        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Integer numeroConta = Integer.parseInt(inputNumeroConta.getText().toString());
                Double saldo = Double.parseDouble(inputSaldo.getText().toString());
                Double debito = Double.parseDouble(inputDebito.getText().toString());
                Double credito = Double.parseDouble(inputCredito.getText().toString());
                Double saldoAtual = (saldo - debito + credito);
                String msg="saldo positivo";
                if (saldoAtual < 0.0) {
                    msg="saldo negativo!";
                }
                textResult.setText(msg+"\n"+saldoAtual);
            }
        });
    }
}
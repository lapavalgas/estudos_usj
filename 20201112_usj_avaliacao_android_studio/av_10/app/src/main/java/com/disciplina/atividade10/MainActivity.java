package com.disciplina.atividade10;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputQntd;
    private EditText inputQntdMax;
    private EditText inputQntdMin;
    private Button btnCalcular;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputQntd = findViewById(R.id.inputQntd);
        inputQntdMax = findViewById(R.id.inputQntdMax);
        inputQntdMin = findViewById(R.id.inputQntdMin);
        btnCalcular = findViewById(R.id.btnCalcular);
        textResult = findViewById(R.id.textResult);

        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Integer qntdEstoque = Integer.parseInt(inputQntd.getText().toString());
                Integer qntdMaxEstoque = Integer.parseInt(inputQntdMax.getText().toString());
                Integer qntdMinEstoque = Integer.parseInt(inputQntdMin.getText().toString());
                Integer qntdMedia = ((qntdMaxEstoque+qntdMinEstoque)/2);

                String msg = "Não efetuar a compra!";

                if (qntdEstoque < qntdMedia) {
                    msg = "Efetuar a compra!";
                }
                textResult.setText(msg+"\nMéida em estoque: "+qntdMedia.toString());
            }
        });
    }
}
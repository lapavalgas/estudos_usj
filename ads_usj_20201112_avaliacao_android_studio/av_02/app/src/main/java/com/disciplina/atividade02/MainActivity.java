package com.disciplina.atividade02;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private Button buttonCalcular;
    private EditText altura;
    private EditText base;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        altura =  findViewById(R.id.inputAltura);
        base =  findViewById(R.id.inputBase);
        textResult =  findViewById(R.id.textResult);
        buttonCalcular =  findViewById(R.id.btnCalcular);

        buttonCalcular.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Double valorAltura = Double.parseDouble(altura.getText().toString());
                Double valorBase = Double.parseDouble(base.getText().toString());
                Double area = valorAltura * valorBase;
                textResult.setText(area.toString());
            }
        });

    }
}
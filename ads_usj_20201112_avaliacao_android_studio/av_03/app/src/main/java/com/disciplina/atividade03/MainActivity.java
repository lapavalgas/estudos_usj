package com.disciplina.atividade03;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private EditText inputMunicipio;
    private EditText inputBrancos;
    private EditText inputNulos;
    private EditText inputValidos;
    private Button btnCalcular;
    private TextView textResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputMunicipio = findViewById(R.id.inputMunicipio);
        inputBrancos = findViewById(R.id.inputBrancos);
        inputNulos = findViewById(R.id.inputNulos);
        inputValidos = findViewById(R.id.inputValido);
        btnCalcular = findViewById(R.id.btnCalcular);
        textResult = findViewById(R.id.textResult);

        btnCalcular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Integer inputMunicipioValue = Integer.parseInt(inputMunicipio.getText().toString());
                Integer percentilBrancos = percentil(
                        inputMunicipioValue,
                        Integer.parseInt(inputBrancos.getText().toString())
                );
                Integer percentilNulos = percentil(
                        inputMunicipioValue,
                        Integer.parseInt(inputNulos.getText().toString())
                );
                Integer percentilValidos = percentil(
                        inputMunicipioValue,
                        Integer.parseInt(inputValidos.getText().toString())
                );

                textResult.setText(
                        ""+percentilBrancos.toString()+"%"
                        +"\n"+percentilNulos.toString()+"%"
                        +"\n"+percentilValidos.toString()+"%"
                        );
            }
        });
    }

    public Integer percentil(Integer total, Integer parcial){
        return (parcial*100)/total;

    }

/**
 *  100 - 1200
 *    8 - ?
 * 
 * 100?=(reajusute*total)/100
 */


}
package com.example.hide;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    private AlertDialog dialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Button loginButton = (Button) findViewById(R.id.loginButton);
        Button registerButton = (Button) findViewById(R.id.registerButton);
        final EditText userId = (EditText) findViewById(R.id.user_id);
        final EditText userPw = (EditText) findViewById(R.id.user_pw);

        loginButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view){
                String userName = userId.getText().toString();
                String passWord = userPw.getText().toString();

                Response.Listener<String> responseListener = new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        try{
                            JSONObject jsonResponse = new JSONObject(response);
                            boolean success = jsonResponse.getBoolean("success");
                            if(success){
                                AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                                dialog = builder.setMessage("로그인에 성공했습니다.")
                                        .setPositiveButton("확인",null)
                                        .create();
                                dialog.show();
                                Intent intent = new Intent(MainActivity.this,WebViewActivity.class); // 메인 -> 웹뷰
                                MainActivity.this.startActivity(intent);
                                finish();
                            }
                            else{
                                AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                                dialog = builder.setMessage("계정을 다시 확인하세요.")
                                        .setNegativeButton("다시 시도",null)
                                        .create();
                                dialog.show();
                            }
                        }catch(Exception e){
                            e.printStackTrace();
                        }
                    }
                };
                LoginRequest loginRequest = new LoginRequest(userName,passWord,responseListener);
                RequestQueue queue = Volley.newRequestQueue(MainActivity.this);
                queue.add(loginRequest);
            }
        });
//
//        loginButton.setOnClickListener(new View.OnClickListener(){
//            @Override
//            public void onClick(View view){
//                userName = userId.getText().toString();
//                passWord = userPw.getText().toString();
//                Intent loginIntent = new Intent(MainActivity.this,WebViewActivity.class);
//                MainActivity.this.startActivity(loginIntent);
//            }
//        });

        registerButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent registerIntent = new Intent(MainActivity.this,RegisterActivity.class);
                MainActivity.this.startActivity(registerIntent);
            }
        });
    }

    @Override
    protected void onStop(){
        super.onStop();
        if(dialog !=null){
            dialog.dismiss();
            dialog = null;
        }
    }
}

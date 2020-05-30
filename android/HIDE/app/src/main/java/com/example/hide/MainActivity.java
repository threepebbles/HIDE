package com.example.hide;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import java.util.HashMap;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    private AlertDialog dialog;
    private ServerRequestApi serverRequestApi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Button loginButton = (Button) findViewById(R.id.loginButton);
        Button registerButton = (Button) findViewById(R.id.registerButton);
        final EditText userId = (EditText) findViewById(R.id.user_id);
        final EditText userPw = (EditText) findViewById(R.id.user_pw);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://34.64.186.183:8000/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        serverRequestApi = retrofit.create(ServerRequestApi.class);

        loginButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view){
                final String userName = userId.getText().toString();
                final String passWord = userPw.getText().toString();

                Login(userName,passWord);

            }
        });

        registerButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent registerIntent = new Intent(MainActivity.this,RegisterActivity.class);
                MainActivity.this.startActivity(registerIntent);
            }
        });
    }

    public void Login(final String username,final String password){
        HashMap<String, String> data = new HashMap<>();
        data.put("username",username);
        data.put("password",password);
        Call<Key> call = serverRequestApi.Login(data);
        call.enqueue(new Callback<Key>() {
            @Override
            public void onResponse(Call<Key> call, Response<Key> response) {
                if(!response.isSuccessful()) {
                    AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                    if (response.code() == 400) {
                        dialog = builder.setMessage("계정 정보가 올바르지 않습니다.")
                                    .setNegativeButton("확인", null)
                                    .create();
                            dialog.show();
                        return;
                    }
                    if(response.code()==500){
                        dialog = builder.setMessage("서버 내부 오류가 발생했습니다.\n관리자에게 문의하세요")
                                .setNegativeButton("확인", null)
                                .create();
                        dialog.show();
                        return;
                    }
                    dialog = builder.setMessage("Error Code : "+Integer.toString(response.code()))
                            .setNegativeButton("확인", null)
                            .create();
                    dialog.show();
                    return;
                }
                Key keyResponse = response.body();
                String value = keyResponse.getKey();
                String sid = response.headers().get("Set-Cookie");
                if(!value.equals("")){
                    Toast.makeText(MainActivity.this, "로그인 성공!", Toast.LENGTH_SHORT).show();
                    Intent intent = new Intent(MainActivity.this,HideActivity.class);
                                intent.putExtra("key",value);
                                intent.putExtra("username",username);
                                intent.putExtra("session",sid);
                                MainActivity.this.startActivity(intent);
                    finish();
                }
            }

            @Override
            public void onFailure(Call<Key> call, Throwable t) {
                //연결 실패
                AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                dialog = builder.setMessage("서버 연결 실패")
                        .setNegativeButton("확인",null)
                        .create();
                dialog.show();
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

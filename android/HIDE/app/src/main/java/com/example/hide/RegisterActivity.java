package com.example.hide;

import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.HashMap;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class RegisterActivity extends AppCompatActivity {

    EditText userNameText,passwordText,passwordCheckText,emailText;
    Button confirmButton;
    ImageView check_user_null,check_pw_null,check_pw_equal,check_email_valid; // correct form -> icon highlight
    boolean form_user,form_pw,form_email; // 유저이름 null check, pw equals & null check , email valid check (1 -> pass / 0 -> fail)
    private AlertDialog dialog;
    private ServerRequestApi serverRequestApi;
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        //widget id
        userNameText = (EditText) findViewById(R.id.register_id);
        check_user_null = (ImageView) findViewById(R.id.check_user_null);
        passwordText = (EditText) findViewById(R.id.register_pw);
        check_pw_null = (ImageView) findViewById(R.id.check_pw_null);
        passwordCheckText = (EditText) findViewById(R.id.register_check_pw);
        check_pw_equal = (ImageView) findViewById(R.id.check_pw_equal);
        emailText = (EditText) findViewById(R.id.register_email);
        check_email_valid = (ImageView) findViewById(R.id.check_email_null);
        confirmButton = (Button) findViewById(R.id.registerConfirm);

        //icon init setting
        check_user_null.setImageResource(R.drawable.ic_person_white_24dp);
        check_pw_null.setImageResource(R.drawable.ic_lock_open_white_24dp);
        check_pw_equal.setImageResource(R.drawable.ic_check_white_24dp);
        check_email_valid.setImageResource(R.drawable.ic_email_white_24dp);

        // confirm check
        form_user = false;
        form_pw = false;
        form_email = false;

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://34.64.186.183:8000/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        serverRequestApi = retrofit.create(ServerRequestApi.class);

        userNameText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                if(userNameText.getText().toString().equals("")){
                    check_user_null.setImageResource(R.drawable.ic_person_white_24dp);
                    form_user = false;
                }else{
                    check_user_null.setImageResource(R.drawable.ic_person_gold_24dp);
                    form_user = true;
                }
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        passwordText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

                if(passwordText.getText().toString().trim().length()<6){
                    check_pw_null.setImageResource(R.drawable.ic_lock_open_white_24dp);
                    form_pw = false;
                }else{
                    check_pw_null.setImageResource(R.drawable.ic_lock_gold_24dp);
                    if(passwordText.getText().toString().equals(passwordCheckText.getText().toString())){
                        check_pw_equal.setImageResource(R.drawable.ic_check_gold_24dp);
                        form_pw = true;
                    }else{
                        check_pw_equal.setImageResource(R.drawable.ic_check_white_24dp);
                        form_pw = false;
                    }
                }


            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        passwordCheckText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                if(!(passwordCheckText.getText().toString().trim().length()<6)&&passwordText.getText().toString().equals(passwordCheckText.getText().toString())){
                    check_pw_equal.setImageResource(R.drawable.ic_check_gold_24dp);
                    form_pw = true;
                }else{
                    check_pw_equal.setImageResource(R.drawable.ic_check_white_24dp);
                    form_pw = false;
                }
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        emailText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

                if(Patterns.EMAIL_ADDRESS.matcher(emailText.getText().toString()).matches()){
                    check_email_valid.setImageResource(R.drawable.ic_email_gold_24dp);
                    form_email = true;
                }else{
                    check_email_valid.setImageResource(R.drawable.ic_email_white_24dp);
                    form_email = false;
                }
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        confirmButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                String userID = userNameText.getText().toString();
                String userPassword = passwordText.getText().toString();
                String passwordCheck = passwordCheckText.getText().toString();
                String userEmail = emailText.getText().toString();
                AlertDialog.Builder builder = new AlertDialog.Builder(RegisterActivity.this);

                if(!(form_user&&form_pw&&form_email)){
                    String content ="";
                    if(!form_user){
                        content += "사용할 아이디를 입력하세요.";
                    }
                    if(!form_pw){
                        content += "\n비밀번호는 6자리 이상이어야 합니다.";
                    }
                    if(!form_email){
                        content += "\n이메일 형식이 올바르지 않습니다.";
                    }
                    dialog = builder.setMessage(content)
                            .setNegativeButton("확인", null)
                            .create();
                    dialog.show();
                    return;
                }
                Register(userID,userPassword,passwordCheck,userEmail);
            }
        });
    }

    public void Register(String userID,String userPassword,String passwordCheck,String userEmail){
        HashMap<String, String> data = new HashMap<>();
        data.put("username",userID);
        data.put("password1",userPassword);
        data.put("password2",passwordCheck);
        data.put("email",userEmail);
        Call<Key> call = serverRequestApi.Register(data);

        call.enqueue(new Callback<Key>() {
            @Override
            public void onResponse(Call<Key> call, Response<Key> response) {
                if(!response.isSuccessful()) {
                    AlertDialog.Builder builder = new AlertDialog.Builder(RegisterActivity.this);
                    if (response.code() == 400) {
                        try {
                            JSONObject jsonObject = new JSONObject(response.errorBody().string());
                            String content = "";
                            //수정부분
                            String check = "";
                            check = jsonObject.optString("username","");
                            if(!check.equals("")){
                                content += "중복아이디 입니다.\n";
                            }
                            check = jsonObject.optString("password1","");
                            if(!check.equals("")){
                                content += "비밀번호는 6자리 이상이어야 합니다.\n";
                            }
                            check = jsonObject.optString("email","");
                            if(!check.equals("")){
                                content += "이메일이 유효하지 않거나 중복 사용된 이메일입니다.";
                            }
                            dialog = builder.setMessage(content)
                                    .setNegativeButton("확인", null)
                                    .create();
                            dialog.show();
                        } catch (JSONException e) {
                            e.printStackTrace();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
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
                if(!value.equals("")){
                    Toast.makeText(RegisterActivity.this, "회원가입 성공!", Toast.LENGTH_SHORT).show();
                    finish();
                }
            }

            @Override
            public void onFailure(Call<Key> call, Throwable t) {
                //연결 실패
                AlertDialog.Builder builder = new AlertDialog.Builder(RegisterActivity.this);
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

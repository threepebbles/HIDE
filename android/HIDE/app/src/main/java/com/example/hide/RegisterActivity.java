package com.example.hide;

import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegisterActivity extends AppCompatActivity {

    EditText userNameText,passwordText,passwordCheckText,emailText;
    Button confirmButton;
    ImageView check_user_null,check_pw_null,check_pw_equal,check_email_valid; // correct form -> icon highlight
    boolean form_user,form_pw,form_email; // 유저이름 null check, pw equals & null check , email valid check (1 -> pass / 0 -> fail)
    private String userID;
    private String userPassword;
    private String userEmail;
    private AlertDialog dialog;
    private boolean validate = true;

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

//        final Button validateButton = (Button)findViewById(R.id.validateButton);
//
//        validateButton.setOnClickListener(new View.OnClickListener(){
//
//            @Override
//            public void onClick(View view){
//                String userID = userNameText.getText().toString();
//                if(validate){
//                    return;
//                }
//                if(userID.equals("")){
//                    AlertDialog.Builder builder = new AlertDialog.Builder(RegisterActivity.this);
//                    dialog = builder.setMessage("아이디는 빈 칸일 수 없습니다.")
//                            .setPositiveButton("확인",null)
//                            .create();
//                    dialog.show();
//                    return;
//                }
//                Response.Listener<String> responseListener = new Response.Listener<String>(){
//
//                    @Override
//                    public void onResponse(String response){
//                        try{
//                            JSONObject jsonResponse = new JSONObject(response);
//                            boolean success = jsonResponse.getBoolean("success");
//                            if(success){
//                                AlertDialog.Builder builder = new AlertDialog.Builder(RegisterActivity.this);
//                                dialog = builder.setMessage("사용할 수 있는 아이디입니다..")
//                                        .setPositiveButton("확인",null)
//                                        .create();
//                                dialog.show();
//                                userNameText.setEnabled(false);
//                                validate = true;
//                                userNameText.setBackgroundColor(getResources().getColor(R.color.colorGray));
//                                validateButton.setBackgroundColor(getResources().getColor(R.color.colorGray));
//                            }
//                            else{
//                                AlertDialog.Builder builder = new AlertDialog.Builder(RegisterActivity.this);
//                                dialog = builder.setMessage("사용할 수 없는 아이디입니다.")
//                                        .setNegativeButton("확인",null)
//                                        .create();
//                                dialog.show();
//                            }
//                        }
//                        catch(Exception e){
//                            e.printStackTrace();
//                        }
//                    }
//                };
//                ValidateRequest validateRequest = new ValidateRequest(userID,responseListener);
//                RequestQueue queue = Volley.newRequestQueue(RegisterActivity.this);
//                queue.add(validateRequest);
//            }
//        });

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

                if(passwordText.getText().toString().equals("")){
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
                if(!passwordCheckText.getText().toString().equals("")&&passwordText.getText().toString().equals(passwordCheckText.getText().toString())){
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

        // confirm 버튼 리스너
        confirmButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                String userID = userNameText.getText().toString();
                String userPassword = passwordText.getText().toString();
                String passwordCheck = passwordCheckText.getText().toString();
                String userEmail = emailText.getText().toString();
                if(!validate){
                    Toast.makeText(RegisterActivity.this, "Please Double Check.", Toast.LENGTH_SHORT).show();
                    return;
                }

                if(!(form_user&&form_pw&&form_email)){
                    Toast.makeText(RegisterActivity.this, "Please Check the Format", Toast.LENGTH_SHORT).show();
                    return;
                }

                Response.Listener<String> responseListener = new Response.Listener<String>(){

                    @Override
                    public void onResponse(String response){
                        try{
                            JSONObject jsonResponse = new JSONObject(response);
                            boolean success = jsonResponse.getBoolean("success");
                            if(success){
                                AlertDialog.Builder builder = new AlertDialog.Builder(RegisterActivity.this);
                                dialog = builder.setMessage("회원가입에 성공했습니다.")
                                        .setPositiveButton("확인",null)
                                        .create();
                                dialog.show();
                                finish();
                            }
                            else{
                                AlertDialog.Builder builder = new AlertDialog.Builder(RegisterActivity.this);
                                dialog = builder.setMessage("회원 등록에 실패했습니다.")
                                        .setNegativeButton("확인",null)
                                        .create();
                                dialog.show();
                            }
                        }
                        catch(Exception e){
                            e.printStackTrace();
                        }
                    }
                };
                RegisterRequest registerRequest = new RegisterRequest(userID,userPassword,passwordCheck,userEmail,responseListener);
                RequestQueue queue = Volley.newRequestQueue(RegisterActivity.this);
                queue.add(registerRequest);
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

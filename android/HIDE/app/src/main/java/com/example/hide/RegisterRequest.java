package com.example.hide;

import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class RegisterRequest extends StringRequest {
    final static private String URL = "http://34.64.186.183:8000/common/signup/"; // 회원가입 서버 주소
    private Map<String, String> parameters;

    public RegisterRequest(String userID, String userPassword, String passwordCheck, String userEmail, Response.Listener<String> listener){
        super(Method.POST,URL,listener,null);
        parameters = new HashMap<>();
        parameters.put("userID",userID);
        parameters.put("userPassword",userPassword);
        parameters.put("PasswordCheck",passwordCheck);
        parameters.put("userEmail",userEmail);
    }

    @Override
    public Map<String,String> getParams(){
        return parameters;
    }
}

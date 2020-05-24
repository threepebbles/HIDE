package com.example.hide;

import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class RegisterRequest extends StringRequest {
    final static private String URL = "http://34.64.186.183:8000/rest-auth/registration/"; // 회원가입 서버 주소
    private Map<String, String> parameters;
//    private Map<String, String> headers;
    public RegisterRequest(String userID, String userPassword, String passwordCheck, String userEmail, Response.Listener<String> listener){
        super(Method.POST,URL,listener,null);
        parameters = new HashMap<>();
//        headers = new HashMap<>();
        parameters.put("username",userID);
        parameters.put("password1",userPassword);
        parameters.put("password2",passwordCheck);
        parameters.put("email",userEmail);
        //headers.put("csrftoken","1");
    }

//    @Override
//    public Map<String, String> getHeaders(){
//        return headers;
//    }

    @Override
    public Map<String,String> getParams(){
        return parameters;
    }
}

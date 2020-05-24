package com.example.hide;

import com.android.volley.Response;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class LogoutRequest extends StringRequest {
    final static private String URL = "http://34.64.186.183:8000/rest-auth/logout/"; // 로그인 서버 주소
    private Map<String, String> parameters;

    public LogoutRequest(String token, Response.Listener<String> listener){
        super(Method.POST,URL,listener,null);
        parameters = new HashMap<>();
        parameters.put("token",token);
    }

    @Override
    public Map<String,String> getParams(){
        return parameters;
    }
}

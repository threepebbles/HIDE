package com.example.hide;

import java.util.HashMap;

import retrofit2.Call;
import retrofit2.http.FieldMap;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public interface ServerRequestApi {

    @FormUrlEncoded
    @POST("rest-auth/registration/")
    Call<Key> Register(@FieldMap HashMap<String,String> data);

    @FormUrlEncoded
    @POST("rest-auth/login/")
    Call<Key> Login(@FieldMap HashMap<String,String> data);

}

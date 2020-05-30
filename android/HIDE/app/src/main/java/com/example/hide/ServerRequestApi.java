package com.example.hide;

import java.util.HashMap;

import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FieldMap;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.HeaderMap;
import retrofit2.http.POST;

public interface ServerRequestApi {

    @FormUrlEncoded
    @POST("rest-auth/registration/")
    Call<Key> Register(@FieldMap HashMap<String,String> data);

    @FormUrlEncoded
    @POST("rest-auth/login/")
    Call<Key> Login(@FieldMap HashMap<String,String> data);

    @FormUrlEncoded
    @POST("rest-auth/logout/")
    Call<Key> Logout(@FieldMap HashMap<String,String> data);

    @POST("hide/myfile/rest/get_network_state/")
    Call<State> NetworkCheck(@HeaderMap HashMap<String,String> token);

    @POST("hide/myfile/rest/get_list/")
    Call<MyFile> ListCheck(@HeaderMap HashMap<String,String> token);

}

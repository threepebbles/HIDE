package com.example.hide;

import android.util.Log;

import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.WebSocket;
import okhttp3.WebSocketListener;
import okio.ByteString;

public class ModifyRequest {
    WebSocket webSocket;
    OkHttpClient client;


    public void Websocket(String token,String path,boolean state){
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        Request request = new Request.Builder()
                .url("ws://34.64.186.183:8000/ws/chat/1/")
                .header("Cookie",token)
                .build();
        client = new OkHttpClient();
        final JSONObject jsonObject = new JSONObject();
        try{
            jsonObject.put("file_path",path);
            jsonObject.put("file_state",state);
        }catch (JSONException e){
            e.printStackTrace();;
        }
        final String jsonString = jsonObject.toString();
        webSocket = client.newWebSocket(request, new WebSocketListener() {
            private static final int NORMAL_CLOSURE_STATUE = 1000;
            @Override
            public void onOpen(WebSocket webSocket, Response response) {
                webSocket.send(jsonString);
            }

            @Override
            public void onMessage(WebSocket webSocket, String text) {
                Log.i("WebSockets","Receiving : "+text);
            }

            @Override
            public void onMessage(WebSocket webSocket, ByteString bytes) {
                Log.i("WebSockets","Receiving bytes: "+bytes);
            }

            @Override
            public void onClosing(WebSocket webSocket, int code, String reason) {
                webSocket.close(NORMAL_CLOSURE_STATUE,null);
            }

            @Override
            public void onFailure(WebSocket webSocket, Throwable t, Response response) {
                Log.i("WebSockets","Error : "+t.getMessage());
            }
        });
    }
}

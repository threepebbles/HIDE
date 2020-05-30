package com.example.hide;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AlertDialog;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import okhttp3.OkHttpClient;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class HideActivity extends AppCompatActivity {

    private ListView pathListView;
    private PathListAdapter adapter;
    private List<PathList> pathList;
    private ServerRequestApi serverRequestApi;
    private AlertDialog dialog;
    private ImageView connect;
    private TextView connectCheck;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hide);

        pathListView = (ListView) findViewById(R.id.pathListView);
        pathList = new ArrayList<PathList>();

        final Button LogoutButton = (Button) findViewById(R.id.LogoutButton);
        Button RefreshButton = (Button) findViewById(R.id.RefreshButton);
        final LinearLayout notice = (LinearLayout) findViewById(R.id.notice);
        final Intent intent = getIntent();
        String username = intent.getExtras().getString("username"); // 사용자정보 출력

        TextView user = (TextView) findViewById(R.id.UserName);
        user.setText("사용자 계정 : "+username);

        final String sid = intent.getExtras().getString("session");

        adapter = new PathListAdapter(getApplicationContext(),pathList,sid);
        pathListView.setAdapter(adapter);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://34.64.186.183:8000/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        serverRequestApi = retrofit.create(ServerRequestApi.class);

        RefreshButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CheckNetwork(sid);
                ListCheck(sid);
            }
        });

        LogoutButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view){
                String token = intent.getExtras().getString("key");
                Logout(token);
            }
        });

        CheckNetwork(sid);
        ListCheck(sid);
    }

    private void Logout(String value){
        HashMap<String,String> data = new HashMap<>();
        data.put("token",value);
        Call<Key> call = serverRequestApi.Logout(data);
        call.enqueue(new Callback<Key>() {
            @Override
            public void onResponse(Call<Key> call, retrofit2.Response<Key> response) {
                if(!response.isSuccessful()) {
                    AlertDialog.Builder builder = new AlertDialog.Builder(HideActivity.this);
                    if (response.code() == 400) {
                        dialog = builder.setMessage("로그아웃에 실패했습니다.")
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
                String value = keyResponse.getDetail();
                if(!value.equals("")) {
                    Toast.makeText(HideActivity.this, "로그아웃 되었습니다.", Toast.LENGTH_SHORT).show();
                    Intent intents = new Intent(HideActivity.this,MainActivity.class);
                    HideActivity.this.startActivity(intents);
                    finish();
                }
            }

            @Override
            public void onFailure(Call<Key> call, Throwable t) {
                AlertDialog.Builder builder = new AlertDialog.Builder(HideActivity.this);
                dialog = builder.setMessage("서버 연결 실패")
                        .setNegativeButton("확인",null)
                        .create();
                dialog.show();
            }
        });
    }

    private void CheckNetwork(String token){
        HashMap<String,String> data = new HashMap<>();
        data.put("Cookie",token);
        Call<State> call = serverRequestApi.NetworkCheck(data);
        call.enqueue(new Callback<State>() {
            @Override
            public void onResponse(Call<State> call, Response<State> response) {
                if(!response.isSuccessful()) {
                    AlertDialog.Builder builder = new AlertDialog.Builder(HideActivity.this);
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
                State stateResponse = response.body();
                String value = stateResponse.getResult();
                boolean networkState = stateResponse.isNetwork_state();
                connect = (ImageView) findViewById(R.id.connect);
                connectCheck = (TextView) findViewById(R.id.networkState);
                if(!value.equals("")) {
                    if(networkState){
                        connect.setImageResource(R.drawable.ic_cast_connected_green_55dp);
                        connectCheck.setText("PC Network Connected");
                        connectCheck.setTextColor(Color.GREEN);
                    }else{
                        connect.setImageResource(R.drawable.ic_cast_connected_red_55dp);
                        connectCheck.setText("PC Network Disconnected");
                        connectCheck.setTextColor(Color.RED);
                    }
                    Toast.makeText(HideActivity.this, ""+networkState, Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<State> call, Throwable t) {
                AlertDialog.Builder builder = new AlertDialog.Builder(HideActivity.this);
                dialog = builder.setMessage("서버 연결 실패")
                        .setNegativeButton("확인",null)
                        .create();
                dialog.show();
            }
        });
    }

    private void ListCheck(String token){
        HashMap<String,String> data = new HashMap<>();
        data.put("Cookie",token);
        Call<MyFile> call = serverRequestApi.ListCheck(data);
        call.enqueue(new Callback<MyFile>() {
            @Override
            public void onResponse(Call<MyFile> call, Response<MyFile> response) {
                AlertDialog.Builder builder = new AlertDialog.Builder(HideActivity.this);
                if(!response.isSuccessful()) {
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
                MyFile myFileResponse = response.body();
                String result = myFileResponse.getResult();
                List<ItemList> itemList = myFileResponse.getItemList();
                String path ;
                boolean state;
                pathList.clear();
                for(ItemList item : itemList){
                    path = item.getFile_path();
                    state = item.isState();
                    PathList filePath = new PathList(path,state);
                    pathList.add(filePath);
                }
                adapter.notifyDataSetChanged();
            }

            @Override
            public void onFailure(Call<MyFile> call, Throwable t) {
                AlertDialog.Builder builder = new AlertDialog.Builder(HideActivity.this);
                dialog = builder.setMessage("서버 연결 실패")
                        .setNegativeButton("확인",null)
                        .create();
                dialog.show();
            }
        });
    }



    private long lastTimeBackPressed;

    @Override
    public void onBackPressed(){
        if(System.currentTimeMillis() - lastTimeBackPressed < 3000){
            finish();
            return;
        }
        Toast.makeText(this,"뒤로 버튼을 한 번 더 눌러 종료합니다.",Toast.LENGTH_SHORT).show();
        lastTimeBackPressed = System.currentTimeMillis();
    }
}

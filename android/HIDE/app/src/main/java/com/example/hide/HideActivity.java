package com.example.hide;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;

public class HideActivity extends AppCompatActivity {

    private ListView pathListView;
    private PathListAdapter adapter;
    private List<PathList> pathList;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hide);

        pathListView = (ListView) findViewById(R.id.pathListView); // 이부분 fragment로 옮겨야함 ListView위치가 기본위치임
        pathList = new ArrayList<PathList>();
        pathList.add(new PathList("C:\\Users\\Jerry\\Desktop\\list",true));
        pathList.add(new PathList("C:\\Users\\Jerry\\Pictures\\Camera Roll",false));
        pathList.add(new PathList("C:\\Users\\Jerry\\Desktop\\savedandroidfile\\compative\\form",true));
        pathList.add(new PathList("C:\\Users\\Jerry\\Desktop\\list",false));
        pathList.add(new PathList("C:\\Users\\Jerry\\Desktop\\list",true));
        adapter = new PathListAdapter(getApplicationContext(),pathList);
        pathListView.setAdapter(adapter);


        final Button InfoButton = (Button) findViewById(R.id.UserInfoButton);
        final Button ListButton = (Button) findViewById(R.id.ListButton);
        final Button LogoutButton = (Button) findViewById(R.id.LogoutButton);
        final LinearLayout notice = (LinearLayout) findViewById(R.id.notice);
        final Intent intent = getIntent();
        String username = intent.getExtras().getString("username"); // 사용자정보 출력
        InfoButton.setText(username);



        InfoButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                notice.setVisibility(View.GONE);
                InfoButton.setBackgroundColor(getResources().getColor(R.color.colorPrimaryDark));
                ListButton.setBackgroundColor(getResources().getColor(R.color.colorGray));
                FragmentManager fragmentManager = getSupportFragmentManager();
                FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
                fragmentTransaction.replace(R.id.fragment,new InfoFragment());
                fragmentTransaction.commit();
            }
        });

        ListButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                notice.setVisibility(View.GONE);
                InfoButton.setBackgroundColor(getResources().getColor(R.color.colorGray));
                ListButton.setBackgroundColor(getResources().getColor(R.color.colorPrimaryDark));
                FragmentManager fragmentManager = getSupportFragmentManager();
                FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
                fragmentTransaction.replace(R.id.fragment,new ListFragment());
                fragmentTransaction.commit();
            }
        });

        LogoutButton.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view){
                String token = intent.getExtras().getString("key");

                Response.Listener<String> responseListener = new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        try{
                            JSONObject jsonResponse = new JSONObject(response);
                            String success = jsonResponse.getString("detail");
                            if(success != null){
                                Toast.makeText(HideActivity.this, "로그아웃에 성공했습니다.", Toast.LENGTH_SHORT).show();
                                Intent intents = new Intent(HideActivity.this,MainActivity.class);
                                HideActivity.this.startActivity(intents);
                                finish();
                            }
                            else{
                                Toast.makeText(HideActivity.this, "로그아웃에 실패했습니다.", Toast.LENGTH_SHORT).show();
                            }
                        }catch(Exception e){
                            e.printStackTrace();
                        }
                    }
                };
                LogoutRequest logoutRequest = new LogoutRequest(token,responseListener);
                RequestQueue queue = Volley.newRequestQueue(HideActivity.this);
                queue.add(logoutRequest);
            }
        });


    }
}

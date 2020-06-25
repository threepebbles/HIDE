package com.example.hide;

import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class PathListAdapter extends BaseAdapter {

    private Context context;
    private List<PathList> pathList;
    private String token;

    public PathListAdapter(Context context, List<PathList> pathList,String token) {
        this.context = context;
        this.pathList = pathList;
        this.token = token;
    }

    @Override
    public int getCount() {
        return pathList.size();
    }

    @Override
    public Object getItem(int position) {
        return pathList.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(final int position, View convertView, ViewGroup parent) {
        View v = View.inflate(context,R.layout.list,null);
        final TextView listPath = (TextView) v.findViewById(R.id.listPath);
        final Switch hideSwitch = (Switch) v.findViewById(R.id.hideSwitch);
        listPath.setText(pathList.get(position).getPath());
        hideSwitch.setChecked(pathList.get(position).isOnOff());
        final ModifyRequest modifyRequest = new ModifyRequest();

        hideSwitch.setOnCheckedChangeListener(new Switch.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                    hideSwitch.setEnabled(false);
                    modifyRequest.Websocket(token,listPath.getText().toString(),isChecked);
                    Toast.makeText(context, "전송완료, 잠시 후 새로고침 해주세요", Toast.LENGTH_SHORT).show();
                }else{
                    hideSwitch.setEnabled(false);
                    modifyRequest.Websocket(token,listPath.getText().toString(),isChecked);
                    Toast.makeText(context, "전송완료, 잠시 후 새로고침 해주세요", Toast.LENGTH_SHORT).show();
                }
            }
        });
        v.setTag(pathList.get(position).getPath());
        return v;
    }



}

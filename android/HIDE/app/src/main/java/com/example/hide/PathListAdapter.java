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

public class PathListAdapter extends BaseAdapter {

    private Context context;
    private List<PathList> pathList;

    public PathListAdapter(Context context, List<PathList> pathList) {
        this.context = context;
        this.pathList = pathList;
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
    public View getView(int position, View convertView, ViewGroup parent) {
        View v = View.inflate(context,R.layout.list,null);
        TextView listPath = (TextView) v.findViewById(R.id.listPath);
        Switch hideSwitch = (Switch) v.findViewById(R.id.hideSwitch);

        listPath.setText(pathList.get(position).getPath());
        hideSwitch.setChecked(pathList.get(position).isOnOff());

        hideSwitch.setOnCheckedChangeListener(new Switch.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked){
                    //여기에다가 이제 신호주고 받아서 성공하면 토스트메시지 출력
                    Toast.makeText(context, "은닉 활성화!", Toast.LENGTH_SHORT).show();
                }else{
                    // 마찬가지
                    Toast.makeText(context, "은닉 비활성화!" + isChecked, Toast.LENGTH_SHORT).show();
                }
            }
        });

        v.setTag(pathList.get(position).getPath());
        return v;
    }



}

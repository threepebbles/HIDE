package com.example.hide;

import com.google.gson.annotations.SerializedName;

import java.util.List;

public class MyFile {

    @SerializedName("result")
    private String result;

    @SerializedName("my_file_list")
    private List<ItemList> itemList = null;

    public MyFile(String result, List<ItemList> itemList) {
        this.result = result;
        this.itemList = itemList;
    }

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public List<ItemList> getItemList() {
        return itemList;
    }

    public void setItemList(List<ItemList> itemList) {
        this.itemList = itemList;
    }
}

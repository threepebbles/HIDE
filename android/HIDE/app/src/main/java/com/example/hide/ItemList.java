package com.example.hide;

import com.google.gson.annotations.SerializedName;

public class ItemList {

    @SerializedName("id")
    private int id;

    @SerializedName("file_path")
    private String file_path;

    @SerializedName("state")
    private boolean state;

    @SerializedName("author_id")
    private int author_id;

    public ItemList(int id, String file_path, boolean state, int author_id) {
        this.id = id;
        this.file_path = file_path;
        this.state = state;
        this.author_id = author_id;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFile_path() {
        return file_path;
    }

    public void setFile_path(String file_path) {
        this.file_path = file_path;
    }

    public boolean isState() {
        return state;
    }

    public void setState(boolean state) {
        this.state = state;
    }

    public int getAuthor_id() {
        return author_id;
    }

    public void setAuthor_id(int author_id) {
        this.author_id = author_id;
    }
}

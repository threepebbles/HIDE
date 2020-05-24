package com.example.hide;

public class PathList {
    private String path;
    private boolean onOff;

    public PathList(String path, boolean onOff) {
        this.path = path;
        this.onOff = onOff;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public boolean isOnOff() {
        return onOff;
    }

    public void setOnOff(boolean onOff) {
        this.onOff = onOff;
    }
}

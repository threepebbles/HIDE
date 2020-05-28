package com.example.hide;

public class State {
    private String result;
    private boolean network_state;

    public State(String result, boolean network_state) {
        this.result = result;
        this.network_state = network_state;
    }

    public String getResult() {
        return result;
    }

    public boolean isNetwork_state() {
        return network_state;
    }
}

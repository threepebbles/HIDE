package com.example.hide;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import androidx.appcompat.app.AppCompatActivity;

public class WebViewActivity extends AppCompatActivity {
    private WebView mWebView;
    private WebSettings mWebSettings;
    private String mUrl = "http://34.64.186.183:8000/";
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_webview);

        mWebView = (WebView)findViewById(R.id.webView);

        mWebView.setWebViewClient(new WebViewClient()); // 클릭시 새창 안뜨게 설정
        mWebSettings = mWebView.getSettings(); //세부 세팅 등록
        mWebSettings.setJavaScriptEnabled(true); // 웹페이지 자바스크립트 허용여부
        mWebSettings.setSupportMultipleWindows(false); //새창 띄우기 허용 여부
        mWebSettings.setJavaScriptCanOpenWindowsAutomatically(false); //자바스크립트 멀티뷰 허용 여부
        mWebSettings.setLoadWithOverviewMode(true);//메타태그 허용 여부
        mWebSettings.setUseWideViewPort(true); // 화면 사이즈 맞추기 허용 여부
        mWebSettings.setSupportZoom(false);//화면줌 허용 여부
        mWebSettings.setBuiltInZoomControls(false);//화면 확대 축소 허용여부
        mWebSettings.setCacheMode(WebSettings.LOAD_DEFAULT);// 브라우저 캐시 허용여부
        mWebSettings.setDomStorageEnabled(false);//로컬저장소 허용여부

        mWebView.loadUrl(mUrl);
    }
}

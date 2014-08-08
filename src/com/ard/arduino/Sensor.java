package com.ard.arduino;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Timer;
import java.util.TimerTask;

import android.app.Activity;
import android.app.AlertDialog;
import android.graphics.Bitmap;
import android.graphics.Bitmap.CompressFormat;
import android.os.Bundle;
import android.os.Environment;
import android.text.format.Time;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.webkit.WebView;
import android.widget.TextView;
import android.widget.Toast;

public class Sensor extends Activity {
	/** Called when the activity is first created. */
	WebView wBrowser;
	Timer timer = new Timer();
	String mydate;
	TextView time;
	
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		wBrowser = (WebView) findViewById(R.id.wBrowser);
		time = (TextView)findViewById(R.id.Time);
		Time today = new Time(Time.getCurrentTimezone());
		today.setToNow();
		time.setText(today.monthDay +"-"+ today.month+1 +"-"+ today.year);
		timer.schedule(new TimerTask() {
			@Override
			public void run() {
				wBrowser.getSettings().setJavaScriptEnabled(true);
				wBrowser.loadUrl("http://192.168.0.10/");
			}
		}, 2000);
		findViewById(R.id.screenShot).setOnClickListener(new OnClickListener() {
			   @Override
			   public void onClick(View v) {
			       Bitmap bitmap = takeScreenshot();
			       saveBitmap(bitmap);
			       Toast.makeText(getApplicationContext(), "picture has been taken", Toast.LENGTH_SHORT).show();
			       
			   }
			});
	};
	
	public Bitmap takeScreenshot() {
		   View rootView = findViewById(android.R.id.content).getRootView();
		   rootView.setDrawingCacheEnabled(true);
		   return rootView.getDrawingCache();
		}

		 public void saveBitmap(Bitmap bitmap) {
			 Time today = new Time(Time.getCurrentTimezone());
			 today.setToNow();
			 
		    File imagePath = new File(Environment.getExternalStorageDirectory() + "/screenshot_"+today.format("%k_%M_%S")+"_.png");
		    FileOutputStream fos;
		    try {
		        fos = new FileOutputStream(imagePath);
		        bitmap.compress(CompressFormat.JPEG, 100, fos);
		        fos.flush();
		        fos.close();
		    } catch (FileNotFoundException e) {
		        Log.e("GREC", e.getMessage(), e);
		    } catch (IOException e) {
		        Log.e("GREC", e.getMessage(), e);
		    }
		}
   
}

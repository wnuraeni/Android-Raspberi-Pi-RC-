package com.ard.arduino;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import com.ard.arduino.R;

public class MenuActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_menu);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.menu, menu);
		return true;
	}

	public void goto_imgdownload(View view){
		Intent intent = new Intent(this,NetworkingActivity.class);
		startActivity(intent);
	}
	public void goto_socket(View view){
		Intent intent = new Intent(this,RCCarActivity.class);
		startActivity(intent);
	}
}

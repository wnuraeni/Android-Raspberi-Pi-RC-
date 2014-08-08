package com.ard.arduino;


import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import com.ard.arduino.R;

public class menu extends Activity {
	Button btsensor, btkamera;
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.menu);
		btsensor = (Button)findViewById(R.id.button2);
		btkamera = (Button)findViewById(R.id.button1);
		fungsibtn();
	}

	private void fungsibtn() {
		btsensor.setOnClickListener(new View.OnClickListener() { 
		    @Override 
		    public void onClick(View v) {
		    	Intent myIntent =  new  Intent(v.getContext(), Sensor.class); 
				startActivityForResult(myIntent, 0); 
		  	}    
		});
		btkamera.setOnClickListener(new View.OnClickListener() { 
		    @Override 
		    public void onClick(View v) {
		    	Intent myIntent =  new  Intent(v.getContext(), RCCarActivity.class); 
				startActivityForResult(myIntent, 0); 
		  	}    
		});
		
	};

}

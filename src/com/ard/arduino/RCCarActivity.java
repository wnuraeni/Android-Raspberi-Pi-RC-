package com.ard.arduino;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.Socket;
import java.net.URI;
import java.net.UnknownHostException;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import android.app.Activity;
import android.media.MediaRecorder;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Environment;
import android.os.ParcelFileDescriptor;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class RCCarActivity extends Activity {

	static final String NICKNAME = "Wei-Meng";
	private static final String TAG = "RcCar";
	InetAddress serverAddress;
	Socket socket;
    long start;
	//--all the views
	static TextView txtMessagesReceived;
	TextView txtMessage;
	private Button btn_forward, btn_backward, btn_left, btn_right, btn_stop, btn_netral;
	private Button btn_cam_up, btn_cam_down, btn_cam_left, btn_cam_right,btn_capture, btn_center, btn_ultrasonic;
	
	//--Camera Viewer
	private MjpegView mv;
	//--Camera url
	private String CameraURL,CameraControlURL;
	private Button btn_record;
	boolean record=false;
	//Ultrasonic
	boolean sonic = true;
	//==========================Execute When RcCarActivity Run=====================
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		//---camera url
		//CameraURL = "http://iris.not.iac.es/axis-cgi/mjpg/video.cgi?resolution=320x240"; //public camera
		CameraURL = "http://192.168.0.1:8080/?action=stream";
		//CameraControlURL = http://192.168.1.10:8081/decoder_control.cgi?user=cxemcar&pwd=cxemcar&command=
		CameraControlURL = "http://192.168.0.1/control?seconds=2&direction=";
		
		//---set layout without title & set layout full screen
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
		
		//---set streaming view
		mv = new MjpegView(this);
		View stolenView = mv;
			
		setContentView(R.layout.activity_rc_car);
	
		View view = (findViewById(R.id.Vid));
		((ViewGroup) view).addView(stolenView);
		
		
		//------get the views
		txtMessage = (TextView)findViewById(R.id.time);
		txtMessagesReceived = (TextView)findViewById(R.id.txtMessageReceived);
		
		//------get the button
		btn_forward = (Button) findViewById(R.id.moveForward);
		btn_backward = (Button) findViewById(R.id.moveBackward);
        btn_left = (Button) findViewById(R.id.moveLeft);
        btn_right = (Button) findViewById(R.id.moveRight);
        btn_stop = (Button) findViewById(R.id.moveStop);
//        btn_netral= (Button) findViewById(R.id.moveCenter);
        
        btn_cam_up = (Button) findViewById(R.id.moveCamUp);
        btn_cam_down = (Button) findViewById(R.id.moveCamDown);
        btn_cam_left = (Button) findViewById(R.id.moveCamLeft);
        btn_cam_right = (Button) findViewById(R.id.moveCamRight);
        btn_capture=(Button) findViewById(R.id.btn_capture);
        btn_center = (Button) findViewById(R.id.btn_center);
        btn_ultrasonic = (Button) findViewById(R.id.ultrasonicOn);
        //btn_record=(Button) findViewById(R.id.btn_record);
        
        //----------set button listener for car controller
        //button forward listener
/*        btn_record.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				Recorder r=new Recorder(CameraURL);
				if(!record){
					((Button)v).setText("Recording");
					Thread t=new Thread(r);
					t.start();
					record=true;
				}else{
					((Button)v).setText("Record");
					r.stopRec();
					record=false;
				}
			}
		});
  */      
        btn_capture.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				mv.capture=true;
				Toast.makeText(getApplicationContext(), "Screenshot Saved", Toast.LENGTH_SHORT).show();
			}
		});
	    btn_forward.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "Forwards";
	        	new WebPageTask().execute(URL);
			}
		});
	    //button backward listener
	    btn_backward.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "Backwards";
	        	new WebPageTask().execute(URL);
			}
		});
	    btn_left.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "Left";
	        	new WebPageTask().execute(URL);
			}
		});
	    btn_right.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "Right";
	        	new WebPageTask().execute(URL);
			}
		});
	    btn_stop.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "Berhenti";
				new WebPageTask().execute(URL);
				
			}
		});
//	    btn_netral.setOnClickListener(new OnClickListener() {
//			
//			@Override
//			public void onClick(View v) {
//				String URL = CameraControlURL + "Netral";
//				new WebPageTask().execute(URL);
//				
//			}
//		});
	    //set ultrasonic button
	    btn_ultrasonic.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				if(sonic){
					start = System.currentTimeMillis();
					String URL = CameraControlURL + "SonicOn";
					new WebPageTask().execute(URL);
					sonic = false;
				}else{
					start = System.currentTimeMillis();
					String URL = CameraControlURL + "SonicOff";
					new WebPageTask().execute(URL);
					sonic = true;
				}
			}
		});
	    //set camera controller
	    btn_cam_up.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "CamUp";
	        	new WebPageTask().execute(URL);
			}
		});
	    btn_cam_down.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "CamDown";
	        	new WebPageTask().execute(URL);
	        	
			}
		});
	    btn_cam_left.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "CamLeft";
	        	new WebPageTask().execute(URL);
			}
		});
	    btn_cam_right.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "CamRight";
	        	new WebPageTask().execute(URL);
			}
		});
	    btn_center.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				start = System.currentTimeMillis();
				String URL = CameraControlURL + "CamCenter";
				new WebPageTask().execute(URL);	
			}
		});
	    //execute read camera streaming
	   new DoRead().execute(CameraURL);
	}
	
	//--- read input stream from webcam
	public class DoRead extends AsyncTask<String, Void, MjpegInputStream>{
		protected MjpegInputStream doInBackground(String... url){
			//camera authentication handler
			HttpResponse res = null;
			DefaultHttpClient httpclient = new DefaultHttpClient();
			Log.d(TAG,"1. Sending http request");
			System.out.println("tes0");

			try{
				res = httpclient.execute(new HttpGet(URI.create(url[0])));
				Log.d(TAG,"2. Request finished, status = "+res.getStatusLine().getStatusCode());
				if(res.getStatusLine().getStatusCode()==401){
					//turn off camera UAC
					System.out.println("tes1");

					return null;
				}
				return new MjpegInputStream(res.getEntity().getContent());
			}catch(ClientProtocolException e){
				e.printStackTrace();
				Log.d(TAG, "Request failed ClientProtocolException",e);
				//Error connection camera
			}catch(IOException e){
				e.printStackTrace();
				Log.d(TAG,"Request failed-IOException ",e);
			}
			return null;
		}
		protected void onPostExecute(MjpegInputStream result){
			mv.setSource(result);
			mv.setDisplayMode(MjpegView.SIZE_STANDARD);
			mv.showFps(true);
		}
	}
	
    private class WebPageTask extends AsyncTask<String, Void, String> {
        @Override
        protected String doInBackground(String... url) {
          String response = "";
//          for (String url : urls) {
            DefaultHttpClient client = new DefaultHttpClient();
            HttpGet httpGet = new HttpGet(url[0]);
            try {
              HttpResponse execute = client.execute(httpGet);
//              InputStream content = execute.getEntity().getContent();
//
//              BufferedReader buffer = new BufferedReader(new InputStreamReader(content));
//              String s = "";
//              while ((s = buffer.readLine()) != null) {
//                response += s;
//              }

            } catch (Exception e) {
              e.printStackTrace();
            }
//          }
          return response;
        }

        @Override
        protected void onPostExecute(String result) {
        	long end = System.currentTimeMillis();
        	long time = end - start;
        	txtMessage.setText(String.valueOf(time) +" ms");
        }
      }
}

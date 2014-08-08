package com.ard.arduino;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.Socket;
import java.net.URI;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class CopyOfRCCarActivity extends Activity {

	static final String NICKNAME = "Wei-Meng";
	private static final String TAG = "RcCar";
	InetAddress serverAddress;
	Socket socket;
    
	//--all the views
	static TextView txtMessagesReceived;
	EditText txtMessage;
	private Button btn_forward, btn_backward, btn_left, btn_right;

	
	//--Camera Viewer
	private MjpegView mv;
	//--Camera url
	private String CameraURL,CameraControlURL;
	
	//==========================Execute When RcCarActivity Run=====================
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		//---camera url
		CameraURL = "http://iris.not.iac.es/axis-cgi/mjpg/video.cgi?resolution=320x240"; //public camera
		//CameraURL = "http://36.72.138.112:8081/webcam/";
		//CameraURL = "http://192.168.0.1:8080/?action=stream";
		//CameraControlURL = http://192.168.1.10:8081/decoder_control.cgi?user=cxemcar&pwd=cxemcar&command=
		CameraControlURL = "http://192.168.1.100/control?seconds=2&direction=";
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
		txtMessage = (EditText)findViewById(R.id.txtMessage);
		txtMessagesReceived = (TextView)findViewById(R.id.txtMessageReceived);
		
		//------get the button
		btn_forward = (Button) findViewById(R.id.moveForward);
		btn_backward = (Button) findViewById(R.id.moveBackward);
        btn_left = (Button) findViewById(R.id.moveLeft);
        btn_right = (Button) findViewById(R.id.moveRight);
        
        
        //----------set button listener for car controller
        //button forward listener
//	    btn_forward.setOnTouchListener(new OnTouchListener() {
//			public boolean onTouch(View v, MotionEvent event) {
//				if(event.getAction() == MotionEvent.ACTION_DOWN) {
//		        	String URL = CameraControlURL + "Forwards";
//		        	new WebPageTask().execute(URL);
//		        } else if (event.getAction() == MotionEvent.ACTION_UP) {
//		        	String URL = CameraControlURL + "Stop";
//		        	new WebPageTask().execute(URL);
//		        }
//				return false;
//			}
//	    });
	    btn_forward.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				String URL = CameraControlURL + "Forwards";
	        	new WebPageTask().execute(URL);
			}
		});
	    //button backward listener
//	    btn_backward.setOnTouchListener(new OnTouchListener() {
//			public boolean onTouch(View v, MotionEvent event) {
//				if(event.getAction() == MotionEvent.ACTION_DOWN) {
//		        	String URL = CameraControlURL + "Backwards";
//		        	new WebPageTask().execute(URL);
//		        } else if (event.getAction() == MotionEvent.ACTION_UP) {
//		        	String URL = CameraControlURL + "Stop";
//		        	new WebPageTask().execute(URL);
//		        }
//				return false;
//		    }
//		});
	    btn_backward.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				String URL = CameraControlURL + "Backwards";
	        	new WebPageTask().execute(URL);
			}
		});
	    
	    //set camera controller
	    
	    //execute read camera streaming
	   new DoRead().execute(CameraURL);
	}
//private final MyHandler mHandler = new MyHandler(this);
//	
//	private final static Runnable sRunnable = new Runnable() {
//		public void run() { }
//	};
//	
//	private void ShowTextDebug(String txtDebug){
//		TextView textCmdSend = (TextView) findViewById(R.id.textViewCmdSend);
//		if(show_Debug){
//	        textCmdSend.setText(String.valueOf("Send:" + txtDebug));
//        }
//        else{
//        	textCmdSend.setText("");
//        }
//	}
//	public void onResume(){
//		super.onResume();
//	}
//	public void onPause(){
//		super.onPause();
//	}
	//--- read input steram from webcam
	public class DoRead extends AsyncTask<String, Void, MjpegInputStream>{
		protected MjpegInputStream doInBackground(String... url){
			//camera authentication handler
			HttpResponse res = null;
			DefaultHttpClient httpclient = new DefaultHttpClient();
			Log.d(TAG,"1. Sending http request");
			try{
				res = httpclient.execute(new HttpGet(URI.create(url[0])));
				Log.d(TAG,"2. Request finished, status = "+res.getStatusLine().getStatusCode());
				if(res.getStatusLine().getStatusCode()==401){
					//turn off camera UAC
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
        protected String doInBackground(String... urls) {
          String response = "";
          for (String url : urls) {
            DefaultHttpClient client = new DefaultHttpClient();
            HttpGet httpGet = new HttpGet(url);
            try {
              HttpResponse execute = client.execute(httpGet);
              InputStream content = execute.getEntity().getContent();

              BufferedReader buffer = new BufferedReader(new InputStreamReader(content));
              String s = "";
              while ((s = buffer.readLine()) != null) {
                response += s;
              }

            } catch (Exception e) {
              e.printStackTrace();
            }
          }
          return response;
        }

        @Override
        protected void onPostExecute(String result) {
          //textView.setText(result);
        }
      }
}

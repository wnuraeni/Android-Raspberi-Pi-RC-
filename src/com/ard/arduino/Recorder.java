package com.ard.arduino;

import java.io.File;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

import android.media.MediaRecorder;
import android.os.Environment;
import android.os.ParcelFileDescriptor;
import android.util.Log;
import android.widget.Button;

public class Recorder implements Runnable{
	MediaRecorder recorder ;
	String CameraURL;
	boolean record=true;
	public Recorder(String url) {
		// TODO Auto-generated constructor stub
		recorder= new MediaRecorder();
		CameraURL=url;
	}
	@Override
	public void run() {
		// TODO Auto-generated method stub
		
			int port = 8080;

			Socket socket=null;
			try {
				socket = new Socket(InetAddress.getByName(CameraURL), port);
			} catch (UnknownHostException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

			ParcelFileDescriptor pfd = ParcelFileDescriptor.fromSocket(socket);

			

			// Additional MediaRecorder setup (output format ... etc.) omitted

			recorder.setOutputFile(pfd.getFileDescriptor());
			
			recorder.setOutputFormat(MediaRecorder.OutputFormat.MPEG_4);
			String filename=System.nanoTime()+"";
			//Bitmap bm = viewStreaming.getDrawingCache();
			File filepath = new File(Environment.getExternalStorageDirectory()+"/DCIM/Simori/Video/Simori_"+filename+".avi");
			
			recorder.setOutputFile(filepath.getAbsolutePath());
			try {
				recorder.prepare();
			} catch (IllegalStateException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

			recorder.start();
			while(record){
				Log.d("Recorder", "Recording...");
			}
			recorder.stop();
	}
	public void stopRec(){
		record=false;
	}
}

package com.ard.arduino;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;

import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.widget.ImageView;

public class NetworkingActivity extends Activity {
	
	ImageView img;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_networking);
		new DownloadImageTask().execute("http://www.mayoff.com/5-01cablecarDCP01934.jpg");
	}

	private InputStream OpenHttpConnection(String urlString)throws IOException
	{
		InputStream in = null;
		int response = -1;
		URL url = new URL(urlString);
		URLConnection conn = url.openConnection();
		
		if(!(conn instanceof HttpURLConnection))
			throw new IOException ("Not an HTTP connection");
		
		try{
			HttpURLConnection httpConn = (HttpURLConnection) conn;
			httpConn.setAllowUserInteraction(false);
			httpConn.setInstanceFollowRedirects(true);
			httpConn.setRequestMethod("GET");
			httpConn.connect();
			response = httpConn.getResponseCode();
			if(response == HttpURLConnection.HTTP_OK){
				in = httpConn.getInputStream();
			}
		}
		catch(Exception ex){
			Log.d("Networking",ex.getLocalizedMessage());
			throw new IOException("Error connecting");
		}
		return in;
	}
	
	private Bitmap DownloadImage(String URL)
	{
		Bitmap bitmap = null;
		InputStream in = null;
		try{
			in = OpenHttpConnection(URL);
			bitmap = BitmapFactory.decodeStream(in);
			in.close();
		}catch(IOException e1){
			Log.d("NetworkingActivity",e1.getLocalizedMessage());
		}
		return bitmap;
	}
	
	private class DownloadImageTask extends AsyncTask<String, Void, Bitmap>{
		protected Bitmap doInBackground(String... urls){
			return DownloadImage(urls[0]);
		}
		
		protected void onPostExecute(Bitmap result){
			ImageView img = (ImageView) findViewById(R.id.img);
			img.setImageBitmap(result);
		}
	}

}

/*
 * Copyright 2012 Google Inc.
 *
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE file.
 */

package com.skia;

import android.app.ActionBar;
import android.app.Activity;
import android.app.DownloadManager;
import android.content.Context;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;

public class SkiaSampleActivity extends Activity
{
    private TextView mTitle;
    private SkiaSampleView mSampleView;

    private ArrayAdapter<String> mSlideList;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.layout);
        mTitle = (TextView) findViewById(R.id.title_view);
        mSampleView = new SkiaSampleView(this);
        mSlideList = new ArrayAdapter<String>(this, android.R.layout.simple_expandable_list_item_1);

        try {
            System.loadLibrary("SampleApp");

            LinearLayout holder = (LinearLayout) findViewById(R.id.holder);
            holder.addView(mSampleView, new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.MATCH_PARENT));

            setupActionBar();

        } catch (UnsatisfiedLinkError e) {
            mTitle.setText("ERROR: native library could not be loaded");
        }
    }

    private void setupActionBar() {
        ActionBar.OnNavigationListener navigationCallback = new ActionBar.OnNavigationListener() {
            @Override
            public boolean onNavigationItemSelected(int position, long itemId) {
                mSampleView.goToSample(position);
                return true;
            }
        };

        ActionBar actionBar = getActionBar();
        actionBar.setDisplayShowHomeEnabled(false);
        actionBar.setDisplayShowTitleEnabled(false);
        actionBar.setNavigationMode(ActionBar.NAVIGATION_MODE_LIST);
        actionBar.setListNavigationCallbacks(mSlideList, navigationCallback);
    }

    @Override
    protected void onResume () {
        super.onResume();
        if (mSampleView.getWidth() > 0 && mSampleView.getHeight() > 0) {
            //TODO try mSampleView.requestRender() instead
            mSampleView.inval();
        }
    }

    @Override
    public void onDestroy() {
        mSampleView.terminate();
        super.onDestroy();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.action_bar, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
        case R.id.overview:
            mSampleView.showOverview();
            return true;
        case R.id.prev:
            mSampleView.previousSample();
            return true;
        case R.id.next:
            mSampleView.nextSample();
            return true;
        case R.id.toggle_rendering:
            mSampleView.toggleRenderingMode();
            return true;
        case R.id.slideshow:
            mSampleView.toggleSlideshow();
            return true;
        case R.id.fps:
            mSampleView.toggleFPS();
            return true;
        case R.id.tiling:
            mSampleView.toggleTiling();
            return true;
        case R.id.bbox:
            mSampleView.toggleBBox();
            return true;
        case R.id.save_to_pdf:
            mSampleView.saveToPDF();
            return true;
        default:
            return false;
        }
    }

    @Override
    public boolean dispatchKeyEvent(KeyEvent event) {
        final int keycode = event.getKeyCode();
        if (keycode == KeyEvent.KEYCODE_BACK) {
            if (event.getAction() == KeyEvent.ACTION_UP) {
                finish();
            }
            return true;
        }
        return false;
    }

    private static final int SET_TITLE = 1;
    private static final int SET_SLIDES = 2;
    private static final int TOAST_DOWNLOAD = 3;

    private Handler mHandler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
            case SET_TITLE:
                mTitle.setText((String) msg.obj);
                SkiaSampleActivity.this.getActionBar().setSubtitle((String) msg.obj);
                break;
            case SET_SLIDES:
                mSlideList.addAll((String[]) msg.obj);
                break;
            case TOAST_DOWNLOAD:
                Toast.makeText(SkiaSampleActivity.this, (String) msg.obj,
                        Toast.LENGTH_SHORT).show();
                break;
            default:
                break;
            }
        }
    };

    // Called by JNI
    @Override
    public void setTitle(CharSequence title) {
        mHandler.obtainMessage(SET_TITLE, title).sendToTarget();
    }

    // Called by JNI
    public void setSlideList(String[] slideList) {
        mHandler.obtainMessage(SET_SLIDES, slideList).sendToTarget();
    }

    // Called by JNI
    public void addToDownloads(final String title, final String desc, final String path) {
        File file = new File(path);
        final long length = file.exists() ? file.length() : 0;
        if (length == 0) {
            String failed = getString(R.string.save_failed);
            mHandler.obtainMessage(TOAST_DOWNLOAD, failed).sendToTarget();
            return;
        }
        String toast = getString(R.string.file_saved).replace("%s", title);
        mHandler.obtainMessage(TOAST_DOWNLOAD, toast).sendToTarget();
        final DownloadManager manager =
                (DownloadManager) getSystemService(Context.DOWNLOAD_SERVICE);
        new Thread("Add PDF to downloads") {
            @Override
            public void run() {
                final String mimeType = "application/pdf";
                manager.addCompletedDownload(title, desc, true, mimeType, path, length, true);
            }
        }.start();
    }
}

use_relative_paths = True

# Dependencies on outside packages, as needed for developers/bots that use
# "gclient" instead of raw SVN access.
#
# For now, this must be maintained in parallel with "SVN externals"
# dependencies for developers who use raw SVN instead of "gclient".
# See third_party/externals/README
#
deps = {
  "third_party/externals/angle" : "http://angleproject.googlecode.com/svn/trunk@1268",
  "third_party/externals/freetype" : "https://android.googlesource.com/platform/external/freetype.git",
  "third_party/externals/gyp" : "http://gyp.googlecode.com/svn/trunk@1563",
  "third_party/externals/libjpeg" : "http://src.chromium.org/svn/trunk/src/third_party/libjpeg@125399",
  "third_party/externals/jsoncpp" : "http://jsoncpp.svn.sourceforge.net/svnroot/jsoncpp/trunk/jsoncpp@248",
  "third_party/externals/jsoncpp-chromium" : "http://src.chromium.org/svn/trunk/src/third_party/jsoncpp@125399",
  "third_party/externals/libwebp" : "http://src.chromium.org/svn/trunk/src/third_party/libwebp@186718",
}

deps_os = {
  "android": {
    "platform_tools/android/third_party/externals/expat" : "https://android.googlesource.com/platform/external/expat.git",
    "platform_tools/android/third_party/externals/gif" : "https://android.googlesource.com/platform/external/giflib.git",
    "platform_tools/android/third_party/externals/png" : "https://android.googlesource.com/platform/external/libpng.git",
    "platform_tools/android/third_party/externals/jpeg" : "https://android.googlesource.com/platform/external/jpeg.git",
  },
}

#hooks = [
#  {
#    # A change to a .gyp, .gypi, or to GYP itself should run the generator.
#    "pattern": ".",
#    "action": ["python", "trunk/gyp_skia"],
#  },
#]

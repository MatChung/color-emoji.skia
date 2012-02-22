# Core Skia library code.
{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'core',
      'type': 'static_library',
      'msvs_guid': 'B7760B5E-BFA8-486B-ACFD-49E3A6DE8E76',
      'sources': [
        '../src/core/ARGB32_Clamp_Bilinear_BitmapShader.h',
        '../src/core/Sk64.cpp',
        '../src/core/SkAAClip.cpp',
        '../src/core/SkAdvancedTypefaceMetrics.cpp',
        '../src/core/SkAlphaRuns.cpp',
        '../src/core/SkAntiRun.h',
        '../src/core/SkBitmap.cpp',
        '../src/core/SkBitmapProcShader.cpp',
        '../src/core/SkBitmapProcShader.h',
        '../src/core/SkBitmapProcState.cpp',
        '../src/core/SkBitmapProcState.h',
        '../src/core/SkBitmapProcState_matrix.h',
        '../src/core/SkBitmapProcState_matrixProcs.cpp',
        '../src/core/SkBitmapProcState_sample.h',
        '../src/core/SkBitmapSampler.cpp',
        '../src/core/SkBitmapSampler.h',
        '../src/core/SkBitmapSamplerTemplate.h',
        '../src/core/SkBitmapShader16BilerpTemplate.h',
        '../src/core/SkBitmapShaderTemplate.h',
        '../src/core/SkBitmap_scroll.cpp',
        '../src/core/SkBlitBWMaskTemplate.h',
        '../src/core/SkBlitMask_D32.cpp',
        '../src/core/SkBlitRow_D16.cpp',
        '../src/core/SkBlitRow_D32.cpp',
        '../src/core/SkBlitRow_D4444.cpp',
        '../src/core/SkBlitter.cpp',
        '../src/core/SkBlitter_4444.cpp',
        '../src/core/SkBlitter_A1.cpp',
        '../src/core/SkBlitter_A8.cpp',
        '../src/core/SkBlitter_ARGB32.cpp',
        '../src/core/SkBlitter_RGB16.cpp',
        '../src/core/SkBlitter_Sprite.cpp',
        '../src/core/SkBuffer.cpp',
        '../src/core/SkCanvas.cpp',
        '../src/core/SkChunkAlloc.cpp',
        '../src/core/SkClampRange.cpp',
        '../src/core/SkClipStack.cpp',
        '../src/core/SkColor.cpp',
        '../src/core/SkColorFilter.cpp',
        '../src/core/SkColorTable.cpp',
        '../src/core/SkComposeShader.cpp',
        '../src/core/SkConcaveToTriangles.cpp',
        '../src/core/SkConcaveToTriangles.h',
        '../src/core/SkConfig8888.cpp',
        '../src/core/SkConfig8888.h',
        '../src/core/SkCordic.cpp',
        '../src/core/SkCordic.h',
        '../src/core/SkCoreBlitters.h',
        '../src/core/SkCubicClipper.cpp',
        '../src/core/SkCubicClipper.h',
        '../src/core/SkData.cpp',
        '../src/core/SkDebug.cpp',
        '../src/core/SkDeque.cpp',
        '../src/core/SkDevice.cpp',
        '../src/core/SkDither.cpp',
        '../src/core/SkDraw.cpp',
        '../src/core/SkDrawProcs.h',
        '../src/core/SkEdgeBuilder.cpp',
        '../src/core/SkEdgeClipper.cpp',
        '../src/core/SkEdge.cpp',
        '../src/core/SkEdge.h',
        '../src/core/SkFP.h',
        '../src/core/SkFilterProc.cpp',
        '../src/core/SkFilterProc.h',
        '../src/core/SkFlattenable.cpp',
        '../src/core/SkFloat.cpp',
        '../src/core/SkFloat.h',
        '../src/core/SkFloatBits.cpp',
        '../src/core/SkFontHost.cpp',
        '../src/core/SkGeometry.cpp',
        '../src/core/SkGlyphCache.cpp',
        '../src/core/SkGlyphCache.h',
        '../src/core/SkGraphics.cpp',
        '../src/core/SkLineClipper.cpp',
        '../src/core/SkMallocPixelRef.cpp',
        '../src/core/SkMask.cpp',
        '../src/core/SkMaskFilter.cpp',
        '../src/core/SkMath.cpp',
        '../src/core/SkMatrix.cpp',
        '../src/core/SkMetaData.cpp',
        '../src/core/SkMMapStream.cpp',
        '../src/core/SkPackBits.cpp',
        '../src/core/SkPaint.cpp',
        '../src/core/SkPath.cpp',
        '../src/core/SkPathEffect.cpp',
        '../src/core/SkPathHeap.cpp',
        '../src/core/SkPathHeap.h',
        '../src/core/SkPathMeasure.cpp',
        '../src/core/SkPicture.cpp',
        '../src/core/SkPictureFlat.cpp',
        '../src/core/SkPictureFlat.h',
        '../src/core/SkPicturePlayback.cpp',
        '../src/core/SkPicturePlayback.h',
        '../src/core/SkPictureRecord.cpp',
        '../src/core/SkPictureRecord.h',
        '../src/core/SkPixelRef.cpp',
        '../src/core/SkPoint.cpp',
        '../src/core/SkProcSpriteBlitter.cpp',
        '../src/core/SkPtrRecorder.cpp',
        '../src/core/SkQuadClipper.cpp',
        '../src/core/SkQuadClipper.h',
        '../src/core/SkRasterClip.cpp',
        '../src/core/SkRasterizer.cpp',
        '../src/core/SkRect.cpp',
        '../src/core/SkRefDict.cpp',
        '../src/core/SkRegion.cpp',
        '../src/core/SkRegionPriv.h',
        '../src/core/SkRegion_path.cpp',
        '../src/core/SkScalar.cpp',
        '../src/core/SkScalerContext.cpp',
        '../src/core/SkScan.cpp',
        '../src/core/SkScanPriv.h',
        '../src/core/SkScan_AntiPath.cpp',
        '../src/core/SkScan_Antihair.cpp',
        '../src/core/SkScan_Hairline.cpp',
        '../src/core/SkScan_Path.cpp',
        '../src/core/SkShader.cpp',
        '../src/core/SkShape.cpp',
        '../src/core/SkSpriteBlitter_ARGB32.cpp',
        '../src/core/SkSpriteBlitter_RGB16.cpp',
        '../src/core/SkSinTable.h',
        '../src/core/SkSpriteBlitter.h',
        '../src/core/SkSpriteBlitterTemplate.h',
        '../src/core/SkStream.cpp',
        '../src/core/SkString.cpp',
        '../src/core/SkStroke.cpp',
        '../src/core/SkStrokerPriv.cpp',
        '../src/core/SkStrokerPriv.h',
        '../src/core/SkTextFormatParams.h',
        '../src/core/SkTSearch.cpp',
        '../src/core/SkTSort.h',
        '../src/core/SkTemplatesPriv.h',
        '../src/core/SkTypeface.cpp',
        '../src/core/SkTypefaceCache.cpp',
        '../src/core/SkTypefaceCache.h',
        '../src/core/SkUnPreMultiply.cpp',
        '../src/core/SkUtils.cpp',
        '../src/core/SkWriter32.cpp',
        '../src/core/SkXfermode.cpp',

        '../include/core/Sk64.h',
        '../include/core/SkAdvancedTypefaceMetrics.h',
        '../include/core/SkAutoKern.h',
        '../include/core/SkBitmap.h',
        '../include/core/SkBlitRow.h',
        '../include/core/SkBlitter.h',
        '../include/core/SkBounder.h',
        '../include/core/SkBuffer.h',
        '../include/core/SkCanvas.h',
        '../include/core/SkChunkAlloc.h',
        '../include/core/SkClampRange.h',
        '../include/core/SkClipStack.h',
        '../include/core/SkColor.h',
        '../include/core/SkColorFilter.h',
        '../include/core/SkColorPriv.h',
        '../include/core/SkColorShader.h',
        '../include/core/SkComposeShader.h',
        '../include/core/SkData.h',
        '../include/core/SkDeque.h',
        '../include/core/SkDescriptor.h',
        '../include/core/SkDevice.h',
        '../include/core/SkDither.h',
        '../include/core/SkDraw.h',
        '../include/core/SkDrawFilter.h',
        '../include/core/SkDrawLooper.h',
        '../include/core/SkEndian.h',
        '../include/core/SkFDot6.h',
        '../include/core/SkFixed.h',
        '../include/core/SkFlattenable.h',
        '../include/core/SkFloatBits.h',
        '../include/core/SkFloatingPoint.h',
        '../include/core/SkFontHost.h',
        '../include/core/SkGeometry.h',
        '../include/core/SkGraphics.h',
        '../include/core/SkMallocPixelRef.h',
        '../include/core/SkMask.h',
        '../include/core/SkMaskFilter.h',
        '../include/core/SkMath.h',
        '../include/core/SkMatrix.h',
        '../include/core/SkMetaData.h',
        '../include/core/SkMMapStream.h',
        '../include/core/SkOSFile.h',
        '../include/core/SkPackBits.h',
        '../include/core/SkPaint.h',
        '../include/core/SkPath.h',
        '../include/core/SkPathEffect.h',
        '../include/core/SkPathMeasure.h',
        '../include/core/SkPerspIter.h',
        '../include/core/SkPicture.h',
        '../include/core/SkPixelRef.h',
        '../include/core/SkPoint.h',
        '../include/core/SkPtrRecorder.h',
        '../include/core/SkRandom.h',
        '../include/core/SkRasterizer.h',
        '../include/core/SkReader32.h',
        '../include/core/SkRect.h',
        '../include/core/SkRefCnt.h',
        '../include/core/SkRefDict.h',
        '../include/core/SkRegion.h',
        '../include/core/SkScalar.h',
        '../include/core/SkScalarCompare.h',
        '../include/core/SkScalerContext.h',
        '../include/core/SkScan.h',
        '../include/core/SkShader.h',
        '../include/core/SkStream.h',
        '../include/core/SkString.h',
        '../include/core/SkStroke.h',
        '../include/core/SkTArray.h',
        '../include/core/SkTDArray.h',
        '../include/core/SkTDStack.h',
        '../include/core/SkTDict.h',
        '../include/core/SkTRegistry.h',
        '../include/core/SkTScopedPtr.h',
        '../include/core/SkTSearch.h',
        '../include/core/SkTemplates.h',
        '../include/core/SkThread.h',
        '../include/core/SkThread_platform.h',
        '../include/core/SkTime.h',
        '../include/core/SkTLazy.h',
        '../include/core/SkTrace.h',
        '../include/core/SkTypeface.h',
        '../include/core/SkTypes.h',
        '../include/core/SkUnPreMultiply.h',
        '../include/core/SkUnitMapper.h',
        '../include/core/SkUtils.h',
        '../include/core/SkWriter32.h',
        '../include/core/SkXfermode.h',
      ],
      'include_dirs': [
        '../include/config',
        '../include/core',
        '../include/ports',
        '../include/xml',
        '../src/core',
      ],
      'msvs_disabled_warnings': [4244, 4267,4345, 4390, 4554, 4800],
      'conditions': [
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
          'cflags': [
            '-Wno-unused',
            '-Wno-unused-function',
          ],
          'link_settings': {
            'libraries': [
              '-lfreetype',
              '-lpthread',
            ],
          },
        }],
        [ 'skia_os == "mac"', {
          'include_dirs': [
            '../include/utils/mac',
            '../third_party/freetype/include/**',
          ],
          'sources': [
            '../include/utils/mac/SkCGUtils.h',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework',
            ],
          },
        }],
        [ 'skia_os == "ios"', {
          'include_dirs': [
            '../include/utils/ios',
          ],
          'sources': [
            '../include/utils/mac/SkCGUtils.h',
          ],
          'link_settings': {
            'libraries': [
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/CoreFoundation.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/CoreGraphics.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/CoreText.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/UIKit.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/Foundation.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/QuartzCore.framework',
              '/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS4.3.sdk/System/Library/Frameworks/OpenGLES.framework',
            ],
          },
        }],
        [ 'skia_os == "win"', {
          'include_dirs': [
            'config/win',
          ],
          'sources!': [
            '../include/core/SkMMapStream.h',
            '../src/core/SkMMapStream.cpp',
          ],
        }],
        [ 'skia_os == "android"', {
          'dependencies': [
             'android_system.gyp:ft2',
          ],
        }],        
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'config',
          '../include/config',
          '../include/core',
          'ext',
        ],
      },
      'dependencies': [
        'opts.gyp:opts'
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:

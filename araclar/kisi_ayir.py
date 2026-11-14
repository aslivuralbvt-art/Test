#!/usr/bin/env python3
# Fotoğraftaki kişiyi arka plandan ayırır (MediaPipe selfie_multiclass_256x256 modeli).
# Kullanım: python3 araclar/kisi_ayir.py <model.tflite> <girdi.jpg> <cikti.png>
import sys, numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
from PIL import Image, ImageFilter
model, src, out = sys.argv[1:4]
seg = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(
    base_options=BaseOptions(model_asset_path=model), output_confidence_masks=True))
img = Image.open(src).convert('RGB')
res = seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(img)))
bgm = np.squeeze(res.confidence_masks[0].numpy_view())
alpha = np.clip((1 - bgm) * 1.15 - 0.05, 0, 1)
a = Image.fromarray((alpha * 255).astype('uint8')).resize(img.size, Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
rgba = img.copy(); rgba.putalpha(a); rgba.save(out)
print(out, img.size)

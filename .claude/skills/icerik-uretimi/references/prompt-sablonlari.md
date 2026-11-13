# AI görsel ve video prompt şablonları

## Karakter kartı (AI influencer / tekrar eden karakter)

Her promptta aynen kullanılacak sabit tanım:

```
CHARACTER: [name], [age]-year-old [gender], [face shape], [eye color] eyes,
[hair color/length/style], [skin tone], [distinctive detail: freckles, mole, glasses],
signature style: [clothing style], vibe: [personality in 3 words]
```

Örnek:
```
CHARACTER: Defne, 24-year-old woman, oval face, hazel eyes, shoulder-length wavy
dark brown hair with curtain bangs, light olive skin, small silver hoop earrings,
signature style: oversized cozy streetwear, vibe: calm, witty, minimalist
```

## Görsel promptu

```
[CHARACTER veya ana konu], [eylem / poz], [ortam / mekân],
[ışık: soft window light / golden hour / neon], [kamera: 35mm, eye level, close-up],
[stil: photorealistic, iPhone photo, editorial, film grain], [renk paleti],
[en-boy oranı: 9:16 / 4:5 / 1:1]
```

Örnek:
```
Defne (see character), standing in a bright minimalist white bedroom, raising both
arms playfully, wearing a cream sherpa jacket, purple crop top and black wide-leg
jeans, soft natural window light, shot on iPhone, eye-level full-body framing,
photorealistic, subtle film grain, neutral pastel palette, 9:16
```

Araç notları:
- **Midjourney:** sona `--ar 9:16 --style raw --v [sürüm]`; karakter tutarlılığı için referans görsel (`--cref`) kullanılabilir.
- **GPT Image / benzeri sohbet tabanlı modeller:** Düz cümlelerle yaz, istenmeyenleri açıkça söyle ("no text, no watermark").
- **Negatif prompt destekleyen modeller:** `blurry, extra fingers, distorted face, text, watermark, low quality`

## Video promptu (Seedance, Kling, Runway, Higgsfield vb.)

Tek çekim (3–8 sn) olarak yaz; uzun videoyu sahnelere böl.

```
SHOT [n] ([süre] s): [CHARACTER] [tek, net eylem], [ortam].
Camera: [static / slow push-in / handheld / orbit / dolly left].
Lighting: [ışık]. Style: [photorealistic / cinematic / UGC selfie video].
Motion: [hareketin hızı ve detayı]. Aspect ratio: 9:16.
```

Örnek:
```
SHOT 1 (4 s): Defne (see character) dances casually in her bright white bedroom,
swinging her arms to the beat, small smile. Camera: static, phone propped on a
shelf, full-body framing. Lighting: soft daylight from a window. Style: authentic
UGC TikTok video, photorealistic. Motion: natural, relaxed, slight hair movement.
Aspect ratio 9:16.
```

İpuçları:
- Bir çekimde tek ana eylem ve tek kamera hareketi kullan.
- Görselden videoya (image-to-video) çalışırken görseldeki detayları tekrar etme; sadece hareketi ve kamerayı tarif et.
- Konuşan karakter için ses/dudak senkronu ayrı araçta yapılır; senaryodaki repliği ayrıca ver.

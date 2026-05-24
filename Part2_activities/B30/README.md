## B30 – AI Image Watermarking and Detection
### Description:
In this exercise, I used Python to build an AI-generated image and apply an invisible watermark. After that, I edited the image and checked to see if the watermark was still visible.
### Implementation:
The original AI image was stored as `original_B30.png`. I added a secret watermark to the PNG information using Python, and I saved the outcome as `watermarked.png`. After that, I used Python to alter the image by scaling it slightly and saving it as `edited.png` while keeping the watermark metadata.
### Detection Result:
I used a detection script to see if the watermark was still there after I had edited the picture. The result verified to the watermark's survival:
```text
Detected watermark: AI_GENERATED_WATERMARK
```
### Analysis:
This exercise showed how watermarking may be used to recognize AI-generated content even after it has undergone minimal alteration. It also demonstrated how the sort of editing used and the watermarking technique affect the watermark's robustness.
### Evidence:
The files are uploaded in this folder.

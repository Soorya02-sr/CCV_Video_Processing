import os, cv2
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Load MoveNet Thunder (pose detector)
movenet = hub.load("https://tfhub.dev/google/movenet/singlepose/thunder/4")

def keypoints(img):
    """Extract normalized keypoints from image."""
    img = tf.image.resize_with_pad(tf.expand_dims(img, 0), 256, 256)
    out = movenet.signatures["serving_default"](tf.cast(img, tf.int32))
    kpts = out["output_0"].numpy()[0, 0, :, :2]
    kpts -= np.mean(kpts, axis=0)
    return kpts / (np.linalg.norm(kpts) + 1e-6)

def avg_dist(k1, k2):
  return np.mean(np.linalg.norm(k1 - k2, axis=1))

def filter_video(video_path, ref_kp, output_path, percentile=10):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames, dists = [], []

    while True:
        ret, frame = cap.read()
        if not ret: break
        dists.append(avg_dist(ref_kp, keypoints(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))))
        frames.append(frame)
    cap.release()

    thr = np.percentile(dists, percentile)  # auto threshold
    kept = [f for f, d in zip(frames, dists) if d > thr]
    print(f"{len(frames)=}, {len(dists)=}, {len(kept)=}")


    if kept:
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
        [out.write(f) for f in kept]
        out.release()
        print(f"✅ Saved {output_path} ({len(kept)}/{len(frames)} frames kept)")
    else:
        print(f"⚠️ Skipped {video_path}, no frames passed filtering.")


def process_folder(in_folder, ref_image, out_folder, percentile=10):
    os.makedirs(out_folder, exist_ok=True)
    ref_kp = keypoints(cv2.cvtColor(cv2.imread(ref_image), cv2.COLOR_BGR2RGB))
    for f in os.listdir(in_folder):
        if f.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            filter_video(os.path.join(in_folder, f), ref_kp, os.path.join(out_folder, f"{f}"), percentile)

if __name__ == "__main__":
    process_folder(
        input("Input folder: ").strip(),
        input("Reference image: ").strip(),
        input("Output folder: ").strip(),
        float(input("Percentile (e.g. 58 = remove most similar 58%): ").strip())
    )

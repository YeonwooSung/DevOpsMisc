# MediaPipe

[MediaPipe](https://google.github.io/mediapipe/) offers cross-platform, customizable ML solutions for live and streaming media.

- [MediaPipe Pose](https://google.github.io/mediapipe/solutions/pose.html)
- [MediaPipe Object Detection](https://google.github.io/mediapipe/solutions/object_detection.html)
- [MediaPipe Face Mesh](https://google.github.io/mediapipe/solutions/face_mesh.html)
- [MediaPipe Box Tracking](https://google.github.io/mediapipe/solutions/box_tracking.html)

Also, MediaPipe supports [video cropping](https://google.github.io/mediapipe/solutions/autoflip.html), [video feature extraction](https://google.github.io/mediapipe/solutions/youtube_8m.html), etc.

## Running MediaPipe as a Serverless

As the MediaPipe supports AI pipeline that could be ported on the CPU-based environment, we could run the simple media processing AI pipeline as a serverless application by porting the MediaPipe on the AWS Labmda or GCP cloud function.

[Reference blog](https://brndusic.github.io/aws/2021/12/31/running-mediapipe-on-aws-lambda.html)

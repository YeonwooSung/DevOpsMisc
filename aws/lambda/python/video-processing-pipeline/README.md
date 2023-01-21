# Creating Video Processing Pipeline in AWS

This simple project contains 3 steps:

1. [Split videos into frames](#1-split-videos-into-frames)
2. [Select the frames which has humans in it](#2-select-the-frames-which-has-humans-in-it)
3. [Extract information from selected frames by using Rekognition API](#3-extract-information-from-selected-frames-by-using-rekognition-api)

## 1. Split videos into frames

In this step, we will implement a lambda function that downloads a video file from S3 bucket, and then split the video into frames. The frames will be saved in another S3 bucket.

In brief, a lambda function enables you to trigger your code when something happens in AWS ecosystem. In our case we will set our trigger to a bucket in s3. If you are unsure about setting a trigger, go through [this article](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-add-triggers-lam-console.html).

Create a lambda function to tackle the first sub task, splitting video into frames/images. The code for the lambda function could be found in [here](./extract_frames_from_video.py)

### Limited resources

A lambda function has approximately 500 MBs of temp space. Make sure your video file is well under that.
If it’s more than that you can always split your video using any tools like ffmpeg.
Also this task will take some time, hence change the default timeout setting and memory to something like 10 minutes and 1000 Mb.
You can always optimize this later after testing your function runtime.

### Add layer for OpenCV

To use opencv in lambda function you need to add a layer to the lambda function.
Refer to [this article](https://itnext.io/create-a-highly-scalable-image-processing-service-on-aws-lambda-and-api-gateway-in-10-minutes-7cbb2893a479) for how to add a layer.
After adding the lambda layer for opencv scroll down to your lambda function and edit the environment variable.
Add a `PYTHONPATH` variable with the value as `/opt/:/var/runtime`.
The reason for adding `/opt/` is because the lambda layer creation step will by default put the opencv layer at `/opt/` location.

## 2. Select the frames which has humans in it

In this step, we will take images from a bucket, apply a filter and upload them in a target bucket for further processing by rekognition API.

Again, we will add a trigger to the S3 bucket for calling the lambda function.
The trigger for this function is the bucket where you have uploaded images from the video. We want this lambda function to be triggered the moment we upload images to the said bucket.

We can detect humans in an image by using opencv’s default face detection algorithms or train one ourselves in sagemaker.
We will train one model to detect objects in an image using sagemaker here.
Sagemaker already has [pre configured notebooks](https://github.com/aws/amazon-sagemaker-examples) and we will use this one for our task.
Open a sagemaker notebook instance and use the code in the link to create a model.
This is a fairly straight forward method, you can simply do a run all on this jupyter notebook and it will create a model.
It will take some time to run.

After completing the above steps you should see an endpoint being created on your sagemaker dashboard.
Note the name of the endpoint you have created by clicking on endpoint link.

After deploying the Object Detection model on the SageMaker, now we need to create a lambda function to detect humans in the images.
As mentioned above, we should add this lambda function as a trigger to the bucket where we have uploaded images from the video.
The lambda function code could be found [here](./person_detection_when_image_uploaded_to_s3.py).

This function will take an image, invoke the endpoint you have created in previous step and return true if there are people in the image.
Among the predicted items (a list) in our image the first one is person and hence we are doing pred_item[0] == 0 to check whether we have detected a person or not.
Pred_item[1] is a number between 0 to 1 and it can be used as a threshold, i.e. if pred_item[1] is greater than a certain threshold you will consider that your algorithms has successfully identified a person.
The loop breaks if the algorithm identified a person and returns true.

Before we proceed to the next part we need to add a layer of python’s `PIL` module for our image processing bit.
This is exactly same as we added `opencv layer` in previous section.
Add a layer of `PIL` to your lambda function. Remember to add environment vaiable PYTHONPATH as “/opt/:/var/runtime”.

### Deploying Object Detection Model on SageMaker

Clearly, the hardest part in this section would be deploying the Object Detection model on SageMaker.
The deploying process itself is not that hard, but the thing is that you need to make it `efficient`.
Here, the `efficient` means that you need to make sure that the SageMaker endpoint API should be reliable, fast and cheap.
In SageMaker, there are a huge number of options to choose from: Asynchronous Inference, Batch Transform, Real-Time Inference, Serverless Inference, etc.
You should consider all of them first, and choose the most optimal one for your use case.

## 3. Extract information from selected frames by using Rekognition API

After filtering images we are now ready to extract information from the images.
The filtered images are stored in a bucket and ready for processing by rekognition.

Create a lambda function and set trigger to the bucket where you have uploaded your filtered image.
The moment we upload the filtered images to this bucket our third lambda function will be initiated.

Now to upload our results from rekognition we will create a firehose stream using kinesis.
We are creating a delivery stream because we want to deliver our results to a s3 bucket for further analysis.
The only thing important here is setting the stream name as you wish and choosing the destination bucket of your choice for storing the results.
After this we are now ready to edit our lambda function.

The code for the lambda function could be found [here](./call_rekognition_for_further_analysis.py).
As you could see in the code, we are calling the `detect_faces` function from rekognition API.
It will return all faces and along with them attributes identified such as age, gender, emotions, whether wearing a sunglass or not etc.
To learn more about the `detect_faces` function of the rekognition API, refer to [this link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_faces).

In the lambda function, we loop over all faces returned by detect_face and gather information required in a variable called payload and use firehose stream client to put the records in our target s3 bucket.
Remember the target is what you set while creating kinesis delivery stream.

Once you put filtered image in your source bucket this function should execute and you should see the results in your target bucket.

You can have a look at your results in the target s3 bucket.

As an extension, we could add more lambda functions with other features of rekognition API, such as `search_faces_by_image` and `compare_faces` to identify the person in the image.
By orchestrating these functions we can create an AI-powered SaaS pipeline for video processing.

## References

[1] [Creating a Video Processing Pipeline in AWS](https://medium.com/@khitish19/creating-a-video-processing-pipeline-in-aws-a224b4a431de)

[2] [Creating a Video Processing Pipeline in AWS... Part2](https://medium.com/@khitish19/creating-a-video-processing-pipeline-in-aws-part-2-2c861aca0b19)

[3] [Creating a Video Processing Pipeline in AWS... Part3](https://medium.com/@khitish19/creating-a-video-processing-pipeline-in-aws-part-3-d0c3818562bd)

[4] [Rekognition API document](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html)

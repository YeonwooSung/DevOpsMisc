var config = require("./config.json");
var AWS = require("aws-sdk");
var { jobParamsTemplateMP4 } = require("./awsJobParams");

const initAWS = () => {
    const { region, endpoint } = config.aws;

    AWS.config.update({ region });
    AWS.config.mediaconvert = { endpoint };
};

const createJob = (params) => {
    return new AWS.MediaConvert({ apiVersion: "2017-08-29" }).createJob(params).promise();
};

const getParams = () => {
    const template = jobParamsTemplateMP4;

    const { jobQueueARN, iamRoleARN, s3 } = config.aws;
    const { inputFile, outputBucket } = s3;

    const { Settings } = template;

    const { Inputs, OutputGroups } = Settings;

    return {
        ...template,
        Queue: jobQueueARN,
        Role: iamRoleARN,
        Settings: {
            ...Settings,
            Inputs: [
                {
                    ...Inputs[0],
                    FileInput: inputFile,
                },
            ],
            OutputGroups: [
                {
                    Name: "File Group",
                    OutputGroupSettings: {
                        Type: "FILE_GROUP_SETTINGS",
                        FileGroupSettings: {
                            Destination: outputBucket,
                        },
                    },
                    Outputs: OutputGroups[0].Outputs,
                },
            ],
        },
    };
};

const main = async () => {
    initAWS();
    const params = getParams();
    const data = await createJob(params);
    console.log("Job created:", data);
};

main();

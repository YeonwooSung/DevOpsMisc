const jobParamsTemplateMP4 = {
    Queue: "JOB_QUEUE_ARN",
    Role: "IAM_ROLE_ARN",
    Settings: {
        OutputGroups: [
            {
                Name: "File Group",
                OutputGroupSettings: {
                    Type: "FILE_GROUP_SETTINGS",
                    FileGroupSettings: {
                        Destination: "s3://OUTPUT_BUCKET_NAME/",
                    },
                },
                Outputs: [
                    {
                        VideoDescription: {
                            ScalingBehavior: "DEFAULT",
                            TimecodeInsertion: "DISABLED",
                            AntiAlias: "ENABLED",
                            Sharpness: 50,
                            CodecSettings: {
                                Codec: "H_264",
                                H264Settings: {
                                    InterlaceMode: "PROGRESSIVE",
                                    NumberReferenceFrames: 3,
                                    Syntax: "DEFAULT",
                                    Softness: 0,
                                    GopClosedCadence: 1,
                                    GopSize: 90,
                                    Slices: 1,
                                    GopBReference: "DISABLED",
                                    SlowPal: "DISABLED",
                                    SpatialAdaptiveQuantization: "ENABLED",
                                    TemporalAdaptiveQuantization: "ENABLED",
                                    FlickerAdaptiveQuantization: "DISABLED",
                                    EntropyEncoding: "CABAC",
                                    Bitrate: 5000000,
                                    FramerateControl: "SPECIFIED",
                                    RateControlMode: "CBR",
                                    CodecProfile: "MAIN",
                                    Telecine: "NONE",
                                    MinIInterval: 0,
                                    AdaptiveQuantization: "HIGH",
                                    CodecLevel: "AUTO",
                                    FieldEncoding: "PAFF",
                                    SceneChangeDetect: "ENABLED",
                                    QualityTuningLevel: "SINGLE_PASS",
                                    FramerateConversionAlgorithm: "DUPLICATE_DROP",
                                    UnregisteredSeiTimecode: "DISABLED",
                                    GopSizeUnits: "FRAMES",
                                    ParControl: "SPECIFIED",
                                    NumberBFramesBetweenReferenceFrames: 2,
                                    RepeatPps: "DISABLED",
                                    FramerateNumerator: 30,
                                    FramerateDenominator: 1,
                                    ParNumerator: 1,
                                    ParDenominator: 1,
                                },
                            },
                            AfdSignaling: "NONE",
                            DropFrameTimecode: "ENABLED",
                            RespondToAfd: "NONE",
                            ColorMetadata: "INSERT",
                        },
                        AudioDescriptions: [
                            {
                                AudioTypeControl: "FOLLOW_INPUT",
                                CodecSettings: {
                                    Codec: "AAC",
                                    AacSettings: {
                                        AudioDescriptionBroadcasterMix: "NORMAL",
                                        RateControlMode: "CBR",
                                        CodecProfile: "LC",
                                        CodingMode: "CODING_MODE_2_0",
                                        RawFormat: "NONE",
                                        SampleRate: 48000,
                                        Specification: "MPEG4",
                                        Bitrate: 64000,
                                    },
                                },
                                LanguageCodeControl: "FOLLOW_INPUT",
                                AudioSourceName: "Audio Selector 1",
                            },
                        ],
                        ContainerSettings: {
                            Container: "MP4",
                            Mp4Settings: {
                                CslgAtom: "INCLUDE",
                                FreeSpaceBox: "EXCLUDE",
                                MoovPlacement: "PROGRESSIVE_DOWNLOAD",
                            },
                        },
                        NameModifier: "_1",
                    },
                ],
            },
        ],
        AdAvailOffset: 0,
        Inputs: [
            {
                AudioSelectors: {
                    "Audio Selector 1": {
                        Offset: 0,
                        DefaultSelection: "NOT_DEFAULT",
                        ProgramSelection: 1,
                        SelectorType: "TRACK",
                        Tracks: [1],
                    },
                },
                VideoSelector: {
                    ColorSpace: "FOLLOW",
                },
                FilterEnable: "AUTO",
                PsiControl: "USE_PSI",
                FilterStrength: 0,
                DeblockFilter: "DISABLED",
                DenoiseFilter: "DISABLED",
                TimecodeSource: "EMBEDDED",
                FileInput: "s3://INPUT_BUCKET_AND_FILE_NAME",
            },
        ],
        TimecodeConfig: {
            Source: "EMBEDDED",
        },
    },
};

module.exports = { jobParamsTemplateMP4 };

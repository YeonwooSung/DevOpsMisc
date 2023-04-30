# Kubernetes Jobs

Jobs are the mechanism in Kubernetes to run a containerized task that runs to completion.
A job can be used for one-time tasks or for periodic tasks.
Jobs can be used for batch processing, data migration, or other automated tasks.

A Job creates one or more Pods and will continue to retry execution of the Pods until a specified number of them successfully terminate.
As pods successfully complete, the Job tracks the successful completions.
When a specified number of successful completions is reached, the task (ie, Job) is complete.
Deleting a Job will clean up the Pods it created. Suspending a Job will delete its active Pods until the Job is resumed again.

- [simple node.js job](./src/job-1.yaml)
- [simple node.js job with 3 replicas](./src/job-2.yaml)

## CronJob

A CronJob creates Jobs on a repeating schedule.

CronJob is meant for performing regular scheduled actions such as backups, report generation, and so on.
One CronJob object is like one line of a crontab (cron table) file on a Unix system.
It runs a job periodically on a given schedule, written in Cron format.

- [simple cronjob that runs node.js job at 1 AM every day](./src/cronjob-1.yaml)
- [simple cronjob that runs node.js job at 1 AM every day with 3 replicas](./src/cronjob-2.yaml)

### Useful Resources

- [Kubernetes CronJob의 스케줄 변경 시 소급 적용된다?](https://blog.outsider.ne.kr/1662)

## References

- [Kubernetes Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [Kubernetes CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)

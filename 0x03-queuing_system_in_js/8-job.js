export function createPushNotificationsJobs(jobs, queue) {
    if (Array.isArray(jobs)) {
        for (const job of jobs) {
            const queueJob = queue.create('push_notification_code_3', job)
            queueJob.save((err) => {
                if (err){
                    console.log(`Notification job ${queueJob.id } failed: ${err}`);
                    return
                } else {
                    console.log(`Notification job created: ${queueJob.id}`);
                }
            })
            queueJob.on('complete', () => console.log(`Notification job ${queueJob.id} completed`));
            queueJob.on('failed', () => console.log(`Notification job ${queueJob.id} failed: ${error}`));
            queueJob.on('progress', (progress) => {
                console.log(`Notification job ${queueJob.id} ${progress}% complete`); 
            });
        }
    } else {
        throw new Error('Jobs is not an array');
    }
}
import { createQueue } from 'kue';

const objData = {
  phoneNumber: '07038575846',
  message: 'I am Favour',
};

const push_notification_code = createQueue();

const job = push_notification_code.create('push_notification_code', objData);

job.save((err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
})

job.on('complete', () => console.log('Notification job completed')).on('failed', () => console.log('Notification job created'));

# Course Notes

## 6 - EC2 - SAA Level

1. 3/6 - 50%
2. 5/6 - 83%

You have launched an EC2 instance that will host a NodeJS application. After installing all the required software and configured your application, you noted down the EC2 instance public IPv4 so you can access it. Then, you stopped and then started your EC2 instance to complete the application configuration. After restart, you can't access the EC2 instance, and you found that the EC2 instance public IPv4 has been changed. What should you do to assign a fixed public IPv4 to your EC2 instance?

> Allocate an Elastic IP and assign it to your EC2 instance (Elastic IP is a public IPv4 that you own as long as you want and you can attach it to one EC2 instance at a time.)

Spot Fleet is a set of Spot Instances and optionally ...............

> On-Demand Instances (Spot Fleet is a set of Spot Instances and optionally On-demand Instances. It allows you to automatically request Spot Instances with the lowest price.)

You have an application performing big data analysis hosted on a fleet of EC2 instances. You want to ensure your EC2 instances have the highest networking performance while communicating with each other. Which EC2 Placement Group should you choose?

- Spread Placement Group
- Cluster Placement Group
- Partition Placement Group

> Cluster Placement Groups place your EC2 instances next to each other which gives you high-performance computing and networking.

You have a critical application hosted on a fleet of EC2 instances in which you want to achieve maximum availability when there's an AZ failure. Which EC2 Placement Group should you choose?

> Spread Placement Group places your EC2 instances on different physical hardware across different AZs.

Elastic Network Interface (ENI) can be attached to EC2 instances in another AZ.

> False (Elastic Network Interfaces (ENIs) are bounded to a specific AZ. You can not attach an ENI to an EC2 instance in a different AZ.)

#TODO
The following are true regarding EC2 Hibernate, EXCEPT:

- EC2 Instance Root Volume must be an Instance Store volume (To enable EC2 Hibernate, the EC2 Instance Root Volume type must be an EBS volume and must be encrypted to ensure the protection of sensitive content.)

# 8 - High Availability and Scalability: ELB & ASG

1. 15/21 - 71%



## 14 - Amazon S3 Security

8/12

## 15 - CloudFront & AWS Global Accelerator

4/6 - 67% (redo)

You have a CloudFront Distribution that serves your website hosted on a fleet of EC2 instances behind an Application Load Balancer. All your clients are from the United States, but you found that some malicious requests are coming from other countries. What should you do to only allow users from the US and block other countries?

> Use CloudFront Geo Restriction

You have a static website hosted on an S3 bucket. You have created a CloudFront Distribution that points to your S3 bucket to better serve your requests and improve performance. After a while, you noticed that users can still access your website directly from the S3 bucket. You want to enforce users to access the website only through CloudFront. How would you achieve that?

> Configure your CloudFront Distribution and create an Origin Access Control (OAC) then update your S3 Bucket Policy to only accept requests from your CloudFront Distribution.

What does this S3 bucket policy do?

```json
{
  "Version": "2012-10-17",
  "Id": "Mystery policy",
  "Statement": [
    {
      "Sid": "What could it be?",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::examplebucket/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE"
        }
      }
    }
  ]
}
```

> Only allows the S3 bucket content to be accessed from your CloudFront Distribution.

A WordPress website is hosted in a set of EC2 instances in an EC2 Auto Scaling Group and fronted by a CloudFront Distribution which is configured to cache the content for 3 days. You have released a new version of the website and want to release it immediately to production without waiting for 3 days for the cached content to be expired. What is the easiest and most efficient way to solve this?

> CloudFront Cache Invalidation

TODO: Follow Up

A company is deploying a media-sharing website to AWS. They are going to use CloudFront to deliver the context with low latency to their customers where they are located in both US and Europe only. After a while there a huge costs for CloudFront. Which CloudFront feature allows you to decrease costs by targeting only US and Europe?

> CloudFront Price Classes

TODO: Follow Up

A company is migrating a web application to AWS Cloud and they are going to use a set of EC2 instances in an EC2 Auto Scaling Group. The web application is made of multiple components so they will need a host-based routing feature to route to specific web application components. This web application is used by many customers and therefore the web application must have a static IP address so it can be whitelisted by the customers’ firewalls. As the customers are distributed around the world, the web application must also provide low latency to all customers. Which AWS service can help you to assign a static IP address and provide low latency across the globe?

> AWS Global Accelerator + Application Load Balancer

## 16 - AWS Storage Extras

11/17 - 65%

You need to move hundreds of Terabytes into Amazon S3, then process the data using a fleet of EC2 instances. You have a 1 Gbit/s broadband. You would like to move the data faster and possibly processing it while in transit. What do you recommend?

- Use your network
- Use Snowcone
- Use AWS Data Migration
- Use Snowball Edge (correct)

> Snowball Edge is the right answer as it comes with computing capabilities and allows you to pre-process the data while it's being moved into Snowball.

#TODO

You want to expose virtually infinite storage for your tape backups. You want to keep the same software you're using and want an iSCSI compatible interface. What do you use?

> AWS Storage Gateway - Tape Gateway

Your EC2 Windows Servers need to share some data by having a Network File System mounted on them which respects the Windows security mechanisms and has integration with Microsoft Active Directory. What do you recommend?

> Amazon FSx for Windows (File Server)

You have hundreds of Terabytes that you want to migrate to AWS S3 as soon as possible. You tried to use your network bandwidth and it will take around 3 weeks to complete the upload process. What is the recommended approach to using in this situation?

> AWS Snowball Edge

You have a large dataset stored in S3 that you want to access from on-premises servers using the NFS or SMB protocol. Also, you want to authenticate access to these files through on-premises Microsoft AD. What would you use?

> AWS Storage Gateway - S3 File Gateway

You are planning to migrate your company's infrastructure from on-premises to AWS Cloud. You have an on-premises Microsoft Windows File Server that you want to migrate. What is the most suitable AWS service you can use?

> Amazon FSx for Windows (File Server)

#TODO

You would like to have a distributed POSIX compliant file system that will allow you to maximize the IOPS in order to perform some High-Performance Computing (HPC) and genomics computational research. This file system has to easily scale to millions of IOPS. What do you recommend?

> Amazon FSx for Lustre

Which deployment option in the FSx file system provides you with long-term storage that's replicated within AZ?

> Persistent File System (Provides long-term storage where data is replicated within the same AZ. Failed files were replaced within minutes.)

Which of the following protocols is NOT supported by AWS Transfer Family?

> Transport Layer Security (AWS Transfer Family is a managed service for file transfers into and out of S3 or EFS using the FTP protocol, thus TLS is not supported.)

#TODO

A company uses a lot of files and data which is stored in an FSx for Windows File Server storage on AWS. Those files are currently used by the resources hosted on AWS. There’s a requirement for those files to be accessed on-premises with low latency. Which AWS service can help you achieve this?

> FSx File Gateway

#TODO
A Solutions Architect is working on planning the migration of a startup company from on-premises to AWS. Currently, their infrastructure consists of many servers and 30 TB of data hosted on a shared NFS storage. He has decided to use Amazon S3 to host the data. Which AWS service can efficiently migrate the data from on-premises to S3?

> AWS DataSync

Which AWS service is best suited to migrate a large amount of data from an S3 bucket to an EFS file system?

> AWS DataSync

A Machine Learning company is working on a set of datasets that are hosted on S3 buckets. The company decided to release those datasets to the public to be useful for others in their research, but they don’t want to configure the S3 bucket to be public. And those datasets should be exposed over the FTP protocol. What can they do to do the requirement efficiently and with the least effort?

> Use AWS Transfer Family

#TODO
Amazon FSx for NetApp ONTAP is compatible with the following protocols, EXCEPT ………………

> FTP

Which AWS service is best suited when migrating from an on-premises ZFS file system to AWS?

> Amazon FSx for OpenZFS

A company is running Amazon S3 File Gateway to host their data on S3 buckets and is able to mount them on-premises using SMB. The data currently is hosted on S3 Standard storage class and there is a requirement to reduce the costs for S3. So, they have decided to migrate some of those data to S3 Glacier. What is the most efficient way they can use to move the data to S3 Glacier automatically?

> Use S3 Lifecycle Policy

You have on-premises sensitive files and documents that you want to regularly synchronize to AWS to keep another copy. Which AWS service can help you with that?

> AWS DataSync (AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between on-premises storage systems and AWS Storage services, as well as between AWS Storage services.)

## 17 - Decoupling applications: SQS, SNS, Kinesis

10/12 - 83%

You have an e-commerce website and you are preparing for Black Friday which is the biggest sale of the year. You expect that your traffic will increase by 100x. Your website already using an SQS Standard Queue, and you're running a fleet of EC2 instances in an Auto Scaling Group to consume SQS messages. What should you do to prepare your SQS Queue?

> Do nothing, SQS scales automatically

You have an SQS Queue where each consumer polls 10 messages at a time and finishes processing them in 1 minute. After a while, you noticed that the same SQS messages are received by different consumers resulting in your messages being processed more than once. What should you do to resolve this issue?

- Enable Long Polling
- Add DelaySeconds parameter to the messages
- Increase the Visibility Timeout (correct)
- Decrease the Visibility Timeout

> SQS Visibility Timeout is a period of time during which Amazon SQS prevents other consumers from receiving and processing the message again. In Visibility Timeout, a message is hidden only after it is consumed from the queue. Increasing the Visibility Timeout gives more time to the consumer to process the message and prevent duplicate reading of the message. (default: 30 sec., min.: 0 sec., max.: 12 hours)

Which SQS Queue type allows your messages to be processed exactly once and in order?

- SQS Standard Queue
- SQS Dead Letter Queue
- SQS Delay Queue
- SQS FIFO Queue

> SQS FIFO (First-In-First-Out) Queues have all the capabilities of the SQS Standard Queue, plus the following two features. First, The order in which messages are sent and received are strictly preserved and a message is delivered once and remains available until a consumer process and deletes it. Second, duplicated messages are not introduced into the queue.

You have 3 different applications that you'd like to send them the same message. All 3 applications are using SQS. What is the best approach would you choose?

- Use SQS Replication Feature
- Use SNS + SQS Fan Out Pattern
- Send messages individually to 3 SQS queues

> This is a common pattern where only one message is sent to the SNS topic and then "fan-out" to multiple SQS queues. This approach has the following features: it's fully decoupled, no data loss, and you have the ability to add more SQS queues (more applications) over time.

You have a Kinesis data stream with 6 shards provisioned. This data stream usually receiving 5 MB/s of data and sending out 8 MB/s. Occasionally, your traffic spikes up to 2x and you get a ProvisionedThroughputExceeded exception. What should you do to resolve the issue?

> Add more Shards (The capacity limits of a Kinesis data stream are defined by the number of shards within the data stream. The limits can be exceeded by either data throughput or the number of reading data calls. Each shard allows for 1 MB/s incoming data and 2 MB/s outgoing data. You should increase the number of shards within your data stream to provide enough capacity.)

You have a website where you want to analyze clickstream data such as the sequence of clicks a user makes, the amount of time a user spends, and where the navigation begins and how it ends. You decided to use Amazon Kinesis, so you have configured the website to send these clickstream data all the way to a Kinesis data stream. While you checking the data sent to your Kinesis data stream, you found that the users' data is not ordered and the data for one individual user is spread across many shards. How would you fix this problem?

> For each record send to Kinesis add a partition key that represents the identity of the user (Kinesis Data Stream uses the partition key associated with each data record to determine which shard a given data record belongs to. When you use the identity of each user as the partition key, this ensures the data for each user is ordered hence sent to the same shard.)

You are running an application that produces a large amount of real-time data that you want to load into S3 and Redshift. Also, these data need to be transformed before being delivered to their destination. What is the best architecture would you choose?

> Kinesis Data Streams + Kinesis Data Firehose (This is a perfect combo of technology for loading data near real-time data into S3 and Redshift. Kinesis Data Firehose supports custom data transformations using AWS Lambda.)

Which of the following is NOT a supported subscriber for AWS SNS?

> Kinesis Data Streams (Note: Kinesis Data Firehose is now supported, but not Kinesis Data Streams.)

Which AWS service helps you when you want to send email notifications to your users?

> SNS

#TODO
You're running many micro-services applications on-premises and they communicate using a message broker that supports MQTT protocol. You're planning to migrate these applications to AWS without re-engineering the applications and modifying the code. Which AWS service allows you to get a managed message broker that supports the MQTT protocol?

> Amazon MQ supports industry-standard APIs such as JMS and NMS, and protocols for messaging, including AMQP, STOMP, MQTT, and WebSocket.

An e-commerce company is preparing for a big marketing promotion that will bring millions of transactions. Their website is hosted on EC2 instances in an Auto Scaling Group and they are using Amazon Aurora as their database. The Aurora database has a bottleneck and a lot of transactions have been failed in the last promotion they have made as they had a lot of transaction and the Aurora database wasn’t prepared to handle these too many transactions. What do you recommend to handle those transactions and prevent any failed transactions?

> Use SQS as a buffer to write to Aurora

A company is using Amazon Kinesis Data Streams to ingest clickstream data and then do some analytical processes on it. There is a campaign in the next few days and the traffic is unpredictable which might grow up to 100x. What Kinesis Data Stream capacity mode do you recommend?

> On-demand Mode







## 18 - Containers on AWS: ECS, Fargate, ECR & EKS

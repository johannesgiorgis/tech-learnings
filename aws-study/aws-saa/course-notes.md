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

6/8 - 75%

You have multiple Docker-based applications hosted on-premises that you want to migrate to AWS. You don't want to provision or manage any infrastructure; you just want to run your containers on AWS. Which AWS service should you choose?

- ECS in EC2 Launch Mode
- ECR
- AWS Fargate on ECS (answer)

> AWS Fargate allows you to run your containers on AWS without managing any servers.

Amazon Elastic Container Service (ECS) has two Launch Types: .................. and ..................

- Amazon EC2 Launch Type and Fargate Launch Type (correct)
- Amazon EC2 Launch Type and EKS Launch Type
- Fargate Launch Type and EKS Launch Type

You have an application hosted on an ECS Cluster (EC2 Launch Type) where you want your ECS tasks to upload files to an S3 bucket. Which IAM Role for your ECS Tasks should you modify?

- EC2 Instance Profile
- ECS Task Role (correct)

> ECS Task Role is the IAM Role used by the ECS task itself. Use when your container wants to call other AWS services like S3, SQS, etc.

You're planning to migrate a WordPress website running on Docker containers from on-premises to AWS. You have decided to run the application in an ECS Cluster, but you want your docker containers to access the same WordPress website content such as website files, images, videos, etc. What do you recommend to achieve this?

- Mount an EFS Volume (correct)
- Mount an EBS Volume
- Use an EC2 Instance Store

> EFS volume can be shared between different EC2 instances and different ECS Tasks. It can be used as a persistent multi-AZ shared storage for your containers.

You are deploying an application on an ECS Cluster made of EC2 instances. Currently, the cluster is hosting one application that is issuing API calls to DynamoDB successfully. Upon adding a second application, which issues API calls to S3, you are getting authorization issues. What should you do to resolve the problem and ensure proper security?

- Edit the EC2 instance role to add permissions to S3
- Create an IAM task role for the new application (correct)
- Enable the Fargate mode
- Edit the S3 bucket policy to allow the ECS task

You are migrating your on-premises Docker-based applications to Amazon ECS. You were using Docker Hub Container Image Library as your container image repository. Which is an alternative AWS service which is fully integrated with Amazon ECS?

- AWS Fargate
- ECR (correct)
- EKS
- Amazon EC2

> Amazon ECR is a fully managed container registry that makes it easy to store, manage, share, and deploy your container images. It won't help in running your Docker-based applications.

Amazon EKS supports the following node types, EXCEPT ………………..

- Managed Node Groups
- Self-Managed Nodes
- AWS Fargate
- AWS Lambda (correct)

A developer has a running website and APIs on his local machine using containers and he wants to deploy both of them on AWS. The developer is new to AWS and doesn’t know much about different AWS services. Which of the following AWS services allows the developer to build and deploy the website and the APIs in the easiest way according to AWS best practices?

- AWS App Runner (correct)
- EC2 Instances + ALB
- Amazon ECS
- AWS Fargate

## 20 - Serverless Solutions Architecture

7/8 - 87.5%

A startup company plans to run its application on AWS. As a solutions architect, the company hired you to design and implement a fully Serverless REST API. Which technology stack do you recommend?

- API Gateway + Lambda (correct)
- ALB + EC2
- ECS + EBS
- CloudFront + S3

#TODO
The following AWS services have an out of the box caching feature, EXCEPT .................

- API Gateway
- Lambda (correct)
- DynamoDB

> Lambda does not have an out-of-the-box caching feature.

You have a lot of static files stored in an S3 bucket that you want to distribute globally to your users. Which AWS service should you use?

- S3 Cross-Region Replication
- CloudFront (correct)
- Route53
- API Gateway

> Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds. This is a perfect use case for Amazon CloudFront.

#TODO
You have created a DynamoDB table in `ap-northeast-1` and would like to make it available in `eu-west-1`, so you decided to create a DynamoDB Global Table. What needs to be enabled first before you create a DynamoDB Global Table?

- DynamoDB Streams (correct)
- DynamoDB DAX
- DynamoDB Versioning
- DynamoDB Backups

> Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache for DynamoDB that delivers up to a 10x performance improvement – from milliseconds to microseconds – even at millions of requests per second. DAX does all the heavy lifting required to add in-memory acceleration to your DynamoDB tables, without requiring developers to manage cache invalidation, data population, or cluster management.
> Amazon DynamoDB provides the on-demand backup capability to create full backups of your tables for long-term retention and archival for regulatory compliance needs.
> DynamoDB Streams enable DynamoDB to get a changelog and use that changelog to replicate data across replica tables in other AWS Regions.

You have configured a Lambda function to run each time an item is added to a DynamoDB table using DynamoDB Streams. The function is meant to insert messages into the SQS queue for further long processing jobs. Each time the Lambda function is invoked, it seems able to read from the DynamoDB Stream but it isn't able to insert the messages into the SQS queue. What do you think the problem is?

- Lambda can't be used to insert messages into the SQS queue, use an EC2 instance instead
- The Lambda Execution IAM Role is missing permissions (correct)
- The Lambda security group must allow outbound access to SQS
- The SQS security group must be edited to allow AWS Lambda

You would like to create an architecture for a micro-services application whose sole purpose is to encode videos stored in an S3 bucket and store the encoded videos back into an S3 bucket. You would like to make this micro-services application reliable and has the ability to retry upon failures. Each video may take over 25 minutes to be processed. The services used in the architecture should be asynchronous and should have the capability to be stopped for a day and resume the next day from the videos that haven't been encoded yet. Which of the following AWS services would you recommend in this scenario?

- S3 + Lambda
- SNS + EC2
- SQS + EC2 (correct)
- SQS + Lambda

> Amazon SQS allows you to retain messages for days and process them later, while we can take down our EC2 instances.

You are running a photo-sharing website where your images are downloaded from all over the world. Every month you publish a master pack of beautiful mountain images that are over 15 GB in size. The content is currently hosted on an Elastic File System (EFS) file system and distributed by an Application Load Balancer and a set of EC2 instances. Each month, you are experiencing very high traffic which increases the load on your EC2 instances and increases network costs. What do you recommend to reduce EC2 load and network costs without refactoring your website?

- Hosts the master pack into S3
- Enable ALB Caching
- Scale up the EC2 instances
- Create a CloudFront Distribution (correct)

> Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds. Amazon CloudFront can be used in front of an Application Load Balancer.

An AWS service allows you to capture gigabytes of data per second in real-time and deliver these data to multiple consuming applications, with a replay feature.

- Kinesis Data Streams (correct)
- S3
- MQ

> Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. It can continuously capture gigabytes of data per second from hundreds of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.

## 21 - Databases in AWS

10/10 - 100%

Which database helps you store relational datasets, with SQL language compatibility and the capability of processing transactions such as insert, update, and delete?

- RDS

Which AWS service provides you with caching capability that is compatible with Redis API?

- ElastiCache - Amazon ElastiCache is a fully managed in-memory data store, compatible with Redis or Memcached.

You want to migrate an on-premises MongoDB NoSQL database to AWS. You don't want to manage any database servers, so you want to use a managed NoSQL database, preferably Serverless, that provides you with high availability, durability, and reliability, and the capability to take your database global. Which database should you choose?

- DynamoDB - Amazon DynamoDB is a key-value, document, NoSQL database.

You are looking to perform Online Transaction Processing (OLTP). You would like to use a database that has built-in auto-scaling capabilities and provides you with the maximum number of replicas for its underlying storage. What AWS service do you recommend?

- Aurora

> Amazon Aurora is a MySQL and PostgreSQL-compatible relational database. It features a distributed, fault-tolerant, self-healing storage system that auto-scales up to 128TB per database instance. It delivers high performance and availability with up to 15 low-latency read replicas, point-in-time recovery, continuous backup to Amazon S3, and replication across 3 AZs.

As a Solutions Architect, a startup company asked you for help as they are working on an architecture for a social media website where users can be friends with each other, and like each other's posts. The company plan on performing some complicated queries such as "What are the number of likes on the posts that have been posted by the friends of Mike?". Which database do you recommend?

- Amazon Neptune is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets.

You have a set of files, 100MB each, that you want to store in a reliable and durable key-value store. Which AWS service do you recommend?

- S3 - Amazon S3 is indeed a key-value store! (where the key is the full path of the object in the bucket)

A company has an on-premises website that uses ReactJS as its frontend, NodeJS as its backend, and MongoDB for the database. There are some issues with the self-hosted MongoDB database as there is a lot of maintenance required and they don’t have and can’t afford the resources or experience to handle those issues. So, a decision was made to migrate the website to AWS. They have decided to host the frontend ReactJS application in an S3 bucket and the NodeJS backend on a set of EC2 instances. Which AWS service can they use to migrate the MongoDB database that provides them with high scalability and availability without making any code changes?

- DocumentDB

A company using a self-hosted on-premises Apache Cassandra database which they want to migrate to AWS. Which AWS service can they use which provides them with a fully managed, highly available, and scalable Apache Cassandra database?

- Keyspaces

An online payment company is using AWS to host its infrastructure. Due to the application’s nature, they have a strict requirement to store an accurate record of financial transactions such as credit and debit transactions. Those transactions must be stored in secured, immutable, encrypted storage which can be cryptographically verified. Which AWS service is best suited for this use case?

- QLDB

A startup is working on developing a new project to reduce forest fires due to climate change. The startup is developing sensors that will be spread across the entire forest to make some readings such as temperature, humidity, and pressures which will help detect the forest fires before it happens. They are going to have thousands of sensors that are going to store a lot of readings each second. There is a requirement to store those readings and do fast analytics so they can predict if there is a fire. Which AWS service can they use to store those readings?

- Timestream

## 27 - IAM Advanced

3/5 - 60%

You have strong regulatory requirements to only allow fully internally audited AWS services in production. You still want to allow your teams to experiment in a development environment while services are being audited. How can you best set this up?

- Create an AWS Organization and create two Prod and Dev OUs, then Apply an SCP on the Prod OU

You are managing the AWS account for your company, and you want to give one of the developers access to read files from an S3 bucket. You have updated the bucket policy to this, but he still can't access the files in the bucket. What is the problem?

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowsRead",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/Dave"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::static-files-bucket-xxx"
    }
  ]
}
```

- Change resource to `arn:aws:s3:::static-files-bucket-xxx/*` as this is an object-level permission

You have 5 AWS Accounts that you manage using AWS Organizations. You want to restrict access to certain AWS services in each account. How should you do that?

- Using AWS Organizations SCP

Which of the following IAM condition key you can use only to allow API calls from a specified AWS region?

- `aws:RequestedRegion`

#TODO
When configuring permissions for EventBridge to configure a Lambda function as a target you should use ………………….. but when you want to configure a Kinesis Data Streams as a target you should use …………………..

- Resource-Based Policy, Identity-based Policy

## 29 - More Solution Architectures

You are working on a Serverless application where you want to process objects uploaded to an S3 bucket. You have configured S3 Events on your S3 bucket to invoke a Lambda function every time an object has been uploaded. You want to ensure that events that can't be processed are sent to a Dead Letter Queue (DLQ) for further processing. Which AWS service should you use to set up the DLQ?

- Lambda - The Lambda function's invocation is "asynchronous", so the DLQ has to be set on the Lambda function side.

As a Solutions Architect, you have created an architecture for a company that includes the following AWS services: CloudFront, Web Application Firewall (AWS WAF), AWS Shield, Application Load Balancer, and EC2 instances managed by an Auto Scaling Group. Sometimes the company receives malicious requests and wants to block these IP addresses. According to your architecture, Where should you do it?

- AWS WAF

#TODO
Your EC2 instances are deployed in Cluster Placement Group in order to perform High-Performance Computing (HPC). You would like to maximize network performance between your EC2 instances. What should you use?

- Elastic Fabric Adapter


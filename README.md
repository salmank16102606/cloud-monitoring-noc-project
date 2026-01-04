# Cloud Monitoring NOC Project

## Project Overview
This project simulates a **Network Operations Center (NOC)** monitoring system in the cloud.  
It monitors **EC2 instance metrics, application logs, and system status** using AWS CloudWatch and SNS alerts.

## Features
- Real Flask web application deployed on EC2
- CloudWatch metrics monitoring:
  - CPU Utilization
  - Memory Usage
  - Disk Usage
- CloudWatch logs monitoring:
  - Application logs
  - Error simulation with `/error` route
- SNS Email alerts for:
  - High CPU
  - High Memory
  - EC2 System Status
- Real incident simulation using `stress` command

## Folder Structure

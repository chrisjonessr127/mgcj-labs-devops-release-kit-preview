# MGCJ Labs · DevOps Release Kit

A documented starting point for releasing one stateless Docker application to AWS ECS Fargate.

**[Explore the product](https://chrismakriel-technologies.amusedgoby2048.chatgpt.site/)**

This public repository introduces the paid kit and includes a free local tool check. The complete source kit is delivered separately after purchase. Checkout is being prepared; this preview does not offer a paid download.

## What the paid kit includes

- Terraform infrastructure for networking, a load balancer, ECS, ECR, and supporting resources.
- GitHub Actions release workflows using short-lived AWS credentials through OIDC.
- Image digest pinning, release verification, and task-definition rollback scripts.
- Monitoring, cleanup guidance, a sample application, and setup documentation.

## Scope

One stateless Linux/amd64 application listening on port 8080, with a `/health` endpoint. The documented sample uses one task by default and public subnets without a NAT gateway. Customers operate their own AWS accounts and pay their AWS charges. This starter does not include a database, database migrations, or a high-availability design.

Read the [architecture overview](ARCHITECTURE.md) and the website requirements before purchasing. The kit's setup guide determines compatible tool versions; installing a newer version does not establish compatibility.

## Free local tool check

Run from this public repository in Ubuntu / WSL with Python 3.10 or newer:

```bash
python3 preflight.py
```

This check reports installed command versions and whether Docker responds. It does not install software, read credentials, query your AWS account, start a container, or create cloud resources. It is a presence check, not an infrastructure acceptance test.

## About

Created by Christopher Jones at MGCJ Labs, drawing on a background in DevOps for state lotteries.

**[Website and purchase information](https://chrismakriel-technologies.amusedgoby2048.chatgpt.site/)** · **[Creator's GitHub profile](https://github.com/chrisjonessr127)**

The MIT license in this repository applies only to these public preview files. It does not license the separately sold DevOps Release Kit. MGCJ Labs is independent of AWS, GitHub, Docker, and HashiCorp.

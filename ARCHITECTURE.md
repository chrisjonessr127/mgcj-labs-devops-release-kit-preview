# Architecture overview

The paid kit targets one stateless Docker application. This is a conceptual overview, not a copy of its Terraform configuration.

```mermaid
flowchart TD
  G[GitHub Actions] -->|OIDC credentials| A[AWS deployment role]
  A -->|Push image| E[Amazon ECR]
  A -->|Update service| S[ECS Fargate service]
  E -->|Pull pinned image| S
  V[Visitors] --> L[Application Load Balancer]
  L --> S
  S --> C[CloudWatch logs and monitoring]
```

Terraform manages the infrastructure. Release workflows build and publish the container image, update the ECS service, and verify the requested release. A rollback restores a prior application task definition; it does not reverse database migrations or external effects.

The sample uses one task by default, public subnets, and no NAT gateway. HTTPS requires the documented domain and certificate setup. AWS usage is billed to the customer's account; stopping a task alone does not remove every billable resource.

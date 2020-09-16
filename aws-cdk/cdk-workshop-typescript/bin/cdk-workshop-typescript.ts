#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { CdkWorkshopTypescriptStack } from '../lib/cdk-workshop-typescript-stack';

const app = new cdk.App();
new CdkWorkshopTypescriptStack(app, 'CdkWorkshopTypescriptStack');
